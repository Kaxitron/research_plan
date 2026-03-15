#!/usr/bin/env python3
"""
Spaced Repetition Program for AI Alignment Research Plan
SM-2 algorithm · topic activation as you progress · dark theme for 4K OLED
"""

import sys
import ctypes
import json
import re
import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta
from pathlib import Path
from random import shuffle, randint

# ── DPI awareness (before any tk window) ───────────────────────────────────
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

# ── Paths ──────────────────────────────────────────────────────────────────
if getattr(sys, 'frozen', False):
    SCRIPT_DIR = Path(sys.executable).parent
else:
    SCRIPT_DIR = Path(__file__).parent
MD_FILE = SCRIPT_DIR / "spaced-repetition.md"
PROGRESS_FILE = SCRIPT_DIR / "sr-progress.json"

# ── Theme ──────────────────────────────────────────────────────────────────
T = {
    'bg':       '#09090b',
    'bg1':      '#111114',
    'bg2':      '#18181b',
    'bg3':      '#1e1e23',
    'bg4':      '#27272a',
    'border':   '#27272a',
    'border_h': '#3f3f46',
    'text':     '#d4d4d8',
    'text2':    '#a1a1aa',
    'text3':    '#71717a',
    'white':    '#fafafa',
    'green':    '#4ade80',
    'green_d':  '#166534',
    'purple':   '#a78bfa',
    'pink':     '#f472b6',
    'yellow':   '#facc15',
    'blue':     '#60a5fa',
    'orange':   '#fb923c',
    'red':      '#f87171',
    'red_d':    '#7f1d1d',
    'cyan':     '#22d3ee',
}

PHASE_ACCENT = {
    '0B': T['blue'],   '0C': T['blue'],   '0D': T['blue'],
    '1': T['green'],
    '2A': T['purple'], '2B': T['purple'], '2C': T['purple'],
    '2D': T['purple'], '2E': T['purple'],
    '3A': T['pink'],   '3B': T['pink'],   '3C': T['pink'],
    '3D': T['pink'],   '3E': T['pink'],
    '4A': T['yellow'], '4B': T['yellow'], '4C': T['yellow'],
    '4D': T['yellow'], '4E': T['yellow'], '4F': T['yellow'],
    '5A': T['orange'], '5B': T['orange'], '5C': T['orange'], '5D': T['orange'],
    '6A': T['red'],
}

# ── SM-2 (stretched intervals for 10+ min practice problems) ───────────────
#   Standard SM-2 is tuned for quick flashcard recall (~5s per card).
#   These problems take 10-30 min each, so we space reviews much wider.
#
#   Failed (q < 3):  reset to 2 days
#   First success:   Okay 3d · Good 7d · Easy 14d
#   Second success:  Okay 14d · Good 21d · Easy 30d
#   After that:      interval × ease (compounds naturally)
#
FIRST_IV  = {3: 3,  4: 7,  5: 14}
SECOND_IV = {3: 14, 4: 21, 5: 30}

def sm2(quality, reps, ease, interval):
    if quality < 3:
        reps, interval = 0, 2
    else:
        if reps == 0:
            interval = FIRST_IV.get(quality, 3)
        elif reps == 1:
            interval = SECOND_IV.get(quality, 14)
        else:
            interval = round(interval * ease)
        reps += 1
    ease = ease + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    return reps, max(round(ease, 2), 1.3), interval


def interval_label(days):
    if days < 30:
        return f"{days}d"
    elif days < 365:
        return f"{days // 30}mo"
    else:
        return f"{days // 365}y"


# ── Parse markdown ─────────────────────────────────────────────────────────
def parse_md(path):
    text = path.read_text(encoding='utf-8')
    sections, topics, cur = [], [], None
    for line in text.split('\n'):
        m = re.match(r'^## (Phase .+?)$', line)
        if m:
            cur = m.group(1)
            sections.append({'name': cur, 'topics': []})
            continue
        m = re.match(r'^\|\s*(\S+)\s*\|\s*(.+?)\s*\|', line)
        if m and cur:
            tid = m.group(1)
            # Skip header and separator rows
            if tid in ('#',) or tid.startswith('-'):
                continue
            pk = re.match(r'^(\d+\w*)-', tid)
            t = {'id': tid, 'text': m.group(2).strip(),
                 'section': cur, 'pk': pk.group(1) if pk else '0B'}
            topics.append(t)
            sections[-1]['topics'].append(t)
    return sections, topics


# ── Progress ───────────────────────────────────────────────────────────────
def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text('utf-8'))
    return {'active': {}}

def save_progress(data):
    PROGRESS_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), 'utf-8')



# ── Custom toggle switch ──────────────────────────────────────────────────
class Toggle(tk.Canvas):
    W, H = 40, 22

    def __init__(self, parent, on=False, command=None, **kw):
        super().__init__(parent, width=self.W, height=self.H,
                         bg=kw.get('bg', T['bg2']), highlightthickness=0, cursor='hand2')
        self.on = on
        self.command = command
        self._draw()
        self.bind('<Button-1>', self._click)

    def _draw(self):
        self.delete('all')
        bg = T['green'] if self.on else T['bg4']
        r = self.H // 2
        # Pill track
        self.create_oval(1, 1, self.H - 1, self.H - 1, fill=bg, outline='')
        self.create_oval(self.W - self.H + 1, 1, self.W - 1, self.H - 1, fill=bg, outline='')
        self.create_rectangle(r, 1, self.W - r, self.H - 1, fill=bg, outline='')
        # Knob
        cx = self.W - r - 1 if self.on else r + 1
        kr = r - 3
        self.create_oval(cx - kr, r - kr, cx + kr, r + kr, fill=T['white'], outline='')

    def _click(self, _):
        self.on = not self.on
        self._draw()
        if self.command:
            self.command(self.on)


# ── Centered content wrapper ──────────────────────────────────────────────
def make_centered(parent, max_width=1100):
    """Create a centered column inside parent with max width."""
    outer = tk.Frame(parent, bg=T['bg'])
    outer.pack(fill='both', expand=True)
    outer.columnconfigure(0, weight=1)
    outer.columnconfigure(1, weight=0)
    outer.columnconfigure(2, weight=1)
    inner = tk.Frame(outer, bg=T['bg'])
    inner.grid(row=0, column=1, sticky='nsew', pady=0)
    # Force max width via a sizing frame
    sizer = tk.Frame(inner, bg=T['bg'], width=max_width, height=0)
    sizer.pack(fill='x')
    outer.rowconfigure(0, weight=1)
    return inner


# ── App ────────────────────────────────────────────────────────────────────
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Spaced Repetition")
        self.root.configure(bg=T['bg'])
        self.root.state('zoomed')
        self.root.minsize(1200, 800)

        self.sections, self.all_topics = parse_md(MD_FILE)
        self.topic_map = {t['id']: t for t in self.all_topics}
        self.progress = load_progress()
        self.review_queue = []
        self.ci = 0
        self._mw_id = None

        self._build_nav()
        self.main = tk.Frame(self.root, bg=T['bg'])
        self.main.pack(fill='both', expand=True)
        self._go_dashboard()

    # ── Nav ────────────────────────────────────────────────────────────
    def _build_nav(self):
        bar = tk.Frame(self.root, bg=T['bg1'], height=56)
        bar.pack(fill='x')
        bar.pack_propagate(False)

        tk.Label(bar, text="SR", font=('Cascadia Code', 15, 'bold'),
                 fg=T['green'], bg=T['bg1']).pack(side='left', padx=(28, 10))
        tk.Label(bar, text="Spaced Repetition", font=('Segoe UI', 14, 'bold'),
                 fg=T['white'], bg=T['bg1']).pack(side='left')

        right = tk.Frame(bar, bg=T['bg1'])
        right.pack(side='right', padx=28)

        for text, cmd, is_accent in [
            ("Review", self._go_review, True),
            ("Manage", self._go_manage, False),
            ("Dashboard", self._go_dashboard, False),
        ]:
            kw = dict(font=('Segoe UI', 11, 'bold' if is_accent else ''),
                      bd=0, padx=20, pady=7, cursor='hand2', command=cmd)
            if is_accent:
                kw.update(fg=T['bg'], bg=T['green'],
                          activebackground='#3ec96f', activeforeground=T['bg'])
            else:
                kw.update(fg=T['text2'], bg=T['bg3'],
                          activebackground=T['bg4'], activeforeground=T['white'])
            tk.Button(right, text=text, **kw).pack(side='right', padx=4)

        tk.Frame(self.root, bg=T['border'], height=1).pack(fill='x')

    # ── Utilities ──────────────────────────────────────────────────────
    def _clear(self):
        if self._mw_id:
            self.root.unbind('<MouseWheel>', self._mw_id)
            self._mw_id = None
        for w in self.main.winfo_children():
            w.destroy()
        # Reset grid config from manage view
        for c in range(3):
            self.main.columnconfigure(c, weight=0, minsize=0)
        self.main.rowconfigure(0, weight=0)

    def _bind_scroll(self, canvas):
        self._mw_id = self.root.bind('<MouseWheel>',
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    def _section_short(self, name):
        """Shorten 'Phase 2A: ODEs (Lessons 13–18)' → '2A: ODEs'"""
        s = name.replace('Phase ', '')
        m = re.match(r'^(.+?)\s*\(Lesson', s)
        return m.group(1).strip() if m else s

    # ── Dashboard ──────────────────────────────────────────────────────
    def _go_dashboard(self):
        self._clear()
        today = date.today().isoformat()
        active = self.progress.get('active', {})

        due = overdue = mastered = new = 0
        for d in active.values():
            nr = d.get('next_review', '')
            if not nr:
                new += 1
            elif nr <= today:
                due += 1
                if nr < today:
                    overdue += 1
            if d.get('interval', 1) >= 30:
                mastered += 1
        due += new

        # Scrollable canvas
        canvas = tk.Canvas(self.main, bg=T['bg'], highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        scroll_inner = tk.Frame(canvas, bg=T['bg'])
        canvas.create_window((0, 0), window=scroll_inner, anchor='n',
                             tags='inner')

        def _resize(e):
            canvas.itemconfigure('inner', width=e.width)
            canvas.configure(scrollregion=canvas.bbox('all'))
        canvas.bind('<Configure>', _resize)
        scroll_inner.bind('<Configure>',
            lambda _: canvas.configure(scrollregion=canvas.bbox('all')))
        self._bind_scroll(canvas)

        # Centered content
        content = tk.Frame(scroll_inner, bg=T['bg'])
        content.pack(pady=48, padx=40)
        # Constrain width
        tk.Frame(content, bg=T['bg'], width=1000, height=0).pack()

        # Header
        tk.Label(content, text="Dashboard", font=('Segoe UI', 22, 'bold'),
                 fg=T['white'], bg=T['bg']).pack(anchor='w')
        tk.Label(content, text="Your spaced repetition overview",
                 font=('Segoe UI', 11), fg=T['text3'], bg=T['bg']).pack(anchor='w', pady=(4, 32))

        # Stat cards
        cards = tk.Frame(content, bg=T['bg'])
        cards.pack(fill='x', pady=(0, 36))
        cards.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform='s')

        for i, (v, l, c) in enumerate([
            (due, "Due Today", T['green'] if due else T['text3']),
            (overdue, "Overdue", T['red'] if overdue else T['text3']),
            (len(active), "Active", T['blue']),
            (mastered, "Mastered", T['yellow']),
            (len(self.all_topics), "Total", T['text3']),
        ]):
            f = tk.Frame(cards, bg=T['bg2'], padx=20, pady=16,
                         highlightbackground=T['border'], highlightthickness=1)
            f.grid(row=0, column=i, sticky='nsew', padx=(0 if i == 0 else 6, 0))
            tk.Label(f, text=str(v), font=('Cascadia Code', 32, 'bold'),
                     fg=c, bg=T['bg2']).pack(anchor='w')
            tk.Label(f, text=l, font=('Segoe UI', 10), fg=T['text3'],
                     bg=T['bg2']).pack(anchor='w', pady=(2, 0))

        # CTA
        if due > 0:
            session_size = min(due, self.DAILY_CAP)
            cta = tk.Frame(content, bg=T['bg2'], pady=24,
                           highlightbackground=T['border'], highlightthickness=1)
            cta.pack(fill='x', pady=(0, 36))
            cta_text = f"{due} card{'s' if due != 1 else ''} due — today's session: {session_size}"
            tk.Label(cta, text=cta_text,
                     font=('Segoe UI', 13), fg=T['text'], bg=T['bg2']).pack(pady=(0, 12))
            tk.Button(cta, text=f"Start Review ({session_size} cards)",
                      font=('Segoe UI', 13, 'bold'), fg=T['bg'], bg=T['green'],
                      activebackground='#3ec96f', bd=0, padx=32, pady=10,
                      cursor='hand2', command=self._go_review).pack()
        else:
            box = tk.Frame(content, bg=T['bg2'], pady=24,
                           highlightbackground=T['green_d'], highlightthickness=1)
            box.pack(fill='x', pady=(0, 36))
            tk.Label(box, text="All caught up — no cards due today",
                     font=('Segoe UI', 13), fg=T['green'], bg=T['bg2']).pack()

        # Section progress
        tk.Label(content, text="Progress by Section",
                 font=('Segoe UI', 14, 'bold'), fg=T['white'],
                 bg=T['bg']).pack(anchor='w', pady=(0, 16))

        for sec in self.sections:
            st = sec['topics']
            sa = sum(1 for t in st if t['id'] in active)
            total = len(st)
            accent = PHASE_ACCENT.get(st[0]['pk'], T['text3']) if st else T['text3']
            short = self._section_short(sec['name'])

            row = tk.Frame(content, bg=T['bg'], pady=5)
            row.pack(fill='x')
            row.columnconfigure(1, weight=1)

            tk.Label(row, text=short, font=('Segoe UI', 10),
                     fg=T['text2'], bg=T['bg'], anchor='w').grid(row=0, column=0, sticky='w', padx=(0, 16))

            track = tk.Frame(row, bg=T['bg3'], height=6)
            track.grid(row=0, column=1, sticky='ew', padx=(0, 12))
            if total > 0 and sa > 0:
                tk.Frame(track, bg=accent, height=6).place(x=0, y=0, relwidth=sa / total)

            tk.Label(row, text=f"{sa}/{total}", font=('Cascadia Code', 9),
                     fg=T['text3'], bg=T['bg'], width=8, anchor='e').grid(row=0, column=2)

    # ── Manage ─────────────────────────────────────────────────────────
    def _go_manage(self):
        self._clear()

        # Use grid for the two-pane layout so right panel actually expands
        self.main.columnconfigure(0, weight=0)
        self.main.columnconfigure(1, weight=0)
        self.main.columnconfigure(2, weight=1)
        self.main.rowconfigure(0, weight=1)

        # Left panel
        left = tk.Frame(self.main, bg=T['bg1'])
        left.grid(row=0, column=0, sticky='ns')

        tk.Label(left, text="Sections", font=('Segoe UI', 18, 'bold'),
                 fg=T['white'], bg=T['bg1']).pack(anchor='w', padx=24, pady=(24, 4))
        tk.Label(left, text="Select a section to manage topics",
                 font=('Segoe UI', 10), fg=T['text3'],
                 bg=T['bg1']).pack(anchor='w', padx=24, pady=(0, 16))

        btn_row = tk.Frame(left, bg=T['bg1'])
        btn_row.pack(fill='x', padx=24, pady=(0, 12))
        tk.Button(btn_row, text="Activate All", font=('Segoe UI', 10),
                  fg=T['green'], bg=T['green_d'], bd=0, padx=14, pady=5,
                  cursor='hand2', command=lambda: self._bulk(True)).pack(side='left', padx=(0, 6))
        tk.Button(btn_row, text="Deactivate All", font=('Segoe UI', 10),
                  fg=T['red'], bg=T['red_d'], bd=0, padx=14, pady=5,
                  cursor='hand2', command=lambda: self._bulk(False)).pack(side='left')

        lf = tk.Frame(left, bg=T['bg1'])
        lf.pack(fill='both', expand=True, padx=12, pady=(0, 12))

        self.sec_lb = tk.Listbox(lf, bg=T['bg2'], fg=T['text'],
            selectbackground=T['bg4'], selectforeground=T['white'],
            font=('Segoe UI', 11), bd=0, highlightthickness=0,
            activestyle='none', relief='flat', width=40)
        sb = tk.Scrollbar(lf, command=self.sec_lb.yview, bg=T['bg2'],
                          troughcolor=T['bg2'], highlightthickness=0, bd=0)
        self.sec_lb.configure(yscrollcommand=sb.set)
        sb.pack(side='right', fill='y')
        self.sec_lb.pack(side='left', fill='both', expand=True)

        self._populate_sec()
        self.sec_lb.bind('<<ListboxSelect>>', lambda _: self._on_sec())

        # Divider
        tk.Frame(self.main, bg=T['border'], width=1).grid(row=0, column=1, sticky='ns')

        # Right panel — expands to fill remaining space
        right = tk.Frame(self.main, bg=T['bg'])
        right.grid(row=0, column=2, sticky='nsew')

        self.t_hdr = tk.Label(right, text="Select a section",
                              font=('Segoe UI', 18, 'bold'), fg=T['white'], bg=T['bg'])
        self.t_hdr.pack(anchor='w', padx=36, pady=(24, 4))
        self.t_sub = tk.Label(right, text="", font=('Segoe UI', 10),
                              fg=T['text3'], bg=T['bg'])
        self.t_sub.pack(anchor='w', padx=36, pady=(0, 16))

        tc = tk.Frame(right, bg=T['bg'])
        tc.pack(fill='both', expand=True, padx=36, pady=(0, 16))

        self.t_canvas = tk.Canvas(tc, bg=T['bg'], highlightthickness=0)
        tsb = tk.Scrollbar(tc, orient='vertical', command=self.t_canvas.yview,
                           bg=T['bg2'], troughcolor=T['bg2'], highlightthickness=0, bd=0)
        self.t_inner = tk.Frame(self.t_canvas, bg=T['bg'])
        self.t_inner.bind('<Configure>',
            lambda _: self.t_canvas.configure(scrollregion=self.t_canvas.bbox('all')))
        self.t_canvas_win = self.t_canvas.create_window((0, 0), window=self.t_inner, anchor='nw')
        self.t_canvas.configure(yscrollcommand=tsb.set)
        # Resize inner frame width to match canvas width
        def _on_canvas_resize(e):
            self.t_canvas.itemconfigure(self.t_canvas_win, width=e.width)
        self.t_canvas.bind('<Configure>', _on_canvas_resize)
        tsb.pack(side='right', fill='y')
        self.t_canvas.pack(side='left', fill='both', expand=True)
        self._bind_scroll(self.t_canvas)

    def _populate_sec(self):
        self.sec_lb.delete(0, 'end')
        active = self.progress.get('active', {})
        for sec in self.sections:
            sa = sum(1 for t in sec['topics'] if t['id'] in active)
            n = len(sec['topics'])
            mark = "\u2713" if sa == n and n > 0 else ("\u00b7" if sa > 0 else " ")
            short = self._section_short(sec['name'])
            self.sec_lb.insert('end', f"  {mark}   {short}    [{sa}/{n}]")

    def _on_sec(self):
        sel = self.sec_lb.curselection()
        if not sel:
            return
        self._show_topics(self.sections[sel[0]])

    def _show_topics(self, section):
        self.cur_section = section
        short = self._section_short(section['name'])
        self.t_hdr.configure(text=short)

        active = self.progress.get('active', {})
        sa = sum(1 for t in section['topics'] if t['id'] in active)
        self.t_sub.configure(text=f"{sa} of {len(section['topics'])} active")

        for w in self.t_inner.winfo_children():
            w.destroy()

        for topic in section['topics']:
            is_on = topic['id'] in active
            accent = PHASE_ACCENT.get(topic['pk'], T['text3'])

            row = tk.Frame(self.t_inner, bg=T['bg2'], pady=10, padx=16,
                           highlightbackground=T['border'], highlightthickness=1)
            row.pack(fill='x', pady=(0, 4))

            # Top line: toggle + ID + badge
            top = tk.Frame(row, bg=T['bg2'])
            top.pack(fill='x')

            toggle = Toggle(row, on=is_on, bg=T['bg2'],
                command=lambda on, tid=topic['id']: self._toggle(tid, on))
            toggle.pack(in_=top, side='left', padx=(0, 12))

            tk.Label(top, text=topic['id'], font=('Cascadia Code', 10),
                     fg=accent, bg=T['bg3'], padx=8, pady=2).pack(side='left')

            if is_on:
                d = active[topic['id']]
                iv = d.get('interval', 1)
                nr = d.get('next_review', '')
                if nr and nr <= date.today().isoformat():
                    bt, bf = "due", T['green']
                elif not nr:
                    bt, bf = "new", T['cyan']
                else:
                    bt, bf = interval_label(iv), T['text3']
                tk.Label(top, text=bt, font=('Cascadia Code', 9),
                         fg=bf, bg=T['bg3'], padx=8, pady=2).pack(side='right')

            # Topic text + copy button
            tk.Label(row, text=topic['text'], font=('Segoe UI', 11),
                     fg=T['text'], bg=T['bg2'], anchor='w',
                     justify='left').pack(fill='x', padx=(54, 0), pady=(6, 0))
            def _copy_manage(txt=topic['text'], r=row):
                self.root.clipboard_clear()
                self.root.clipboard_append(txt)
            tk.Button(row, text="Copy", font=('Segoe UI', 9),
                      fg=T['text3'], bg=T['bg3'], activebackground=T['bg4'],
                      activeforeground=T['white'], bd=0, padx=8, pady=2,
                      cursor='hand2', command=_copy_manage).pack(anchor='w', padx=(54, 0), pady=(4, 0))

    def _toggle(self, tid, on):
        active = self.progress.setdefault('active', {})
        if on:
            nr = (date.today() + timedelta(days=randint(1, 14))).isoformat()
            active.setdefault(tid, {'ease': 2.5, 'interval': 1,
                                     'repetitions': 0, 'next_review': nr, 'last_review': ''})
        else:
            active.pop(tid, None)
        save_progress(self.progress)
        self._populate_sec()
        if hasattr(self, 'cur_section'):
            sa = sum(1 for t in self.cur_section['topics'] if t['id'] in active)
            self.t_sub.configure(text=f"{sa} of {len(self.cur_section['topics'])} active")

    def _bulk(self, activate):
        sel = self.sec_lb.curselection()
        if not sel:
            messagebox.showinfo("Manage", "Select a section first.")
            return
        sec = self.sections[sel[0]]
        active = self.progress.setdefault('active', {})
        for t in sec['topics']:
            if activate:
                nr = (date.today() + timedelta(days=randint(1, 14))).isoformat()
                active.setdefault(t['id'], {'ease': 2.5, 'interval': 1,
                                             'repetitions': 0, 'next_review': nr, 'last_review': ''})
            else:
                active.pop(t['id'], None)
        save_progress(self.progress)
        self._populate_sec()
        self._show_topics(sec)

    # ── Review ─────────────────────────────────────────────────────────
    DAILY_CAP = 4

    def _go_review(self):
        today = date.today().isoformat()
        active = self.progress.get('active', {})

        # Split into due (overdue + new) and upcoming (not yet due)
        due_q, upcoming_q = [], []
        for tid, d in active.items():
            topic = self.topic_map.get(tid)
            if not topic:
                continue
            nr = d.get('next_review', '')
            if not nr or nr <= today:
                sk = 0 if not nr else -(date.today() - date.fromisoformat(nr)).days
                due_q.append((sk, tid, topic))
            else:
                days_until = (date.fromisoformat(nr) - date.today()).days
                upcoming_q.append((days_until, tid, topic))

        shuffle(due_q)
        upcoming_q.sort()

        self.due_cards = [(tid, t) for _, tid, t in due_q]
        self.upcoming_cards = [(tid, t) for _, tid, t in upcoming_q]
        self.review_queue = self.due_cards[:self.DAILY_CAP]
        self.extra_due = self.due_cards[self.DAILY_CAP:]  # due cards beyond cap
        self.ci = 0
        self.session_total = 0

        if not self.review_queue:
            if self.upcoming_cards:
                self._render_done()  # will offer "review ahead"
            else:
                messagebox.showinfo("Review", "No cards due — you're all caught up!")
            return
        self._render_card()

    def _render_card(self):
        self._clear()

        if self.ci >= len(self.review_queue):
            self._render_done()
            return

        tid, topic = self.review_queue[self.ci]
        d = self.progress['active'][tid]
        total = len(self.review_queue)
        cur = self.ci + 1
        accent = PHASE_ACCENT.get(topic['pk'], T['text3'])
        reps = d.get('repetitions', 0)
        ease = d.get('ease', 2.5)
        iv = d.get('interval', 1)

        # Outer wrapper for centering
        outer = tk.Frame(self.main, bg=T['bg'])
        outer.pack(fill='both', expand=True)
        outer.columnconfigure(0, weight=1)
        outer.columnconfigure(1, weight=0, minsize=1000)
        outer.columnconfigure(2, weight=1)
        outer.rowconfigure(0, weight=1)

        wrapper = tk.Frame(outer, bg=T['bg'])
        wrapper.grid(row=0, column=1, sticky='nsew', pady=24)

        # Top: progress
        top = tk.Frame(wrapper, bg=T['bg'])
        top.pack(fill='x', pady=(0, 8))
        tk.Label(top, text=f"{cur} / {total}", font=('Cascadia Code', 11),
                 fg=T['text3'], bg=T['bg']).pack(side='left')
        tk.Label(top, text=f"{total - cur} remaining", font=('Segoe UI', 10),
                 fg=T['text3'], bg=T['bg']).pack(side='right')

        # Progress track
        track = tk.Frame(wrapper, bg=T['bg3'], height=4)
        track.pack(fill='x', pady=(0, 20))
        tk.Frame(track, bg=T['green'], height=4).place(x=0, y=0, relwidth=cur / total)

        # Card
        card = tk.Frame(wrapper, bg=T['bg2'], padx=56, pady=40,
                        highlightbackground=T['border'], highlightthickness=1)
        card.pack(fill='both', expand=True)

        # Meta
        meta = tk.Frame(card, bg=T['bg2'])
        meta.pack(fill='x', pady=(0, 6))
        tk.Label(meta, text=tid, font=('Cascadia Code', 14, 'bold'),
                 fg=accent, bg=T['bg2']).pack(side='left')
        info = f"interval {iv}d   reps {reps}   ease {ease:.2f}"
        tk.Label(meta, text=info, font=('Cascadia Code', 10),
                 fg=T['text3'], bg=T['bg2']).pack(side='right')

        # Section
        short_sec = self._section_short(topic['section'])
        tk.Label(card, text=short_sec, font=('Segoe UI', 11),
                 fg=T['text3'], bg=T['bg2']).pack(anchor='w', pady=(0, 24))

        # Topic — centered vertically in remaining space
        topic_area = tk.Frame(card, bg=T['bg2'])
        topic_area.pack(fill='both', expand=True)
        tk.Label(topic_area, text=topic['text'], font=('Segoe UI', 22),
                 fg=T['white'], bg=T['bg2'], wraplength=850,
                 justify='left', anchor='w').pack(anchor='w', expand=True)

        # Copy button — includes prompt for Claude
        def _copy_topic(txt=topic['text'], sec=short_sec):
            prompt = (f"Generate practice questions on the following topic that "
                      f"would take about 5 minutes to complete. "
                      f"Include a mix of conceptual and computational questions.\n\n"
                      f"Section: {sec}\n"
                      f"Topic: {txt}")
            self.root.clipboard_clear()
            self.root.clipboard_append(prompt)
            copy_btn.configure(text="Copied!", fg=T['green'])
            self.root.after(1500, lambda: copy_btn.configure(text="Copy Topic", fg=T['text2']))
        copy_btn = tk.Button(topic_area, text="Copy Topic", font=('Segoe UI', 10),
                             fg=T['text2'], bg=T['bg3'], activebackground=T['bg4'],
                             activeforeground=T['white'], bd=0, padx=14, pady=5,
                             cursor='hand2', command=_copy_topic)
        copy_btn.pack(anchor='w', pady=(8, 0))

        # Divider
        tk.Frame(card, bg=T['border'], height=1).pack(fill='x', pady=(24, 20))

        # Rating label
        tk.Label(card, text="Rate your performance on this topic",
                 font=('Segoe UI', 11), fg=T['text3'], bg=T['bg2']).pack(pady=(0, 14))

        # Rating buttons
        btn_row = tk.Frame(card, bg=T['bg2'])
        btn_row.pack()

        ratings = [
            (0, "Again", T['red']),
            (1, "Wrong", '#e05555'),
            (2, "Hard",  T['orange']),
            (3, "Okay",  T['yellow']),
            (4, "Good",  T['blue']),
            (5, "Easy",  T['green']),
        ]

        for q, label, color in ratings:
            _, _, ni = sm2(q, reps, ease, iv)
            bf = tk.Frame(btn_row, bg=T['bg2'])
            bf.pack(side='left', padx=5)
            tk.Button(bf, text=label, font=('Segoe UI', 11, 'bold'),
                fg=color, bg=T['bg3'], activebackground=T['bg4'],
                activeforeground=color, bd=0, width=9, height=2,
                cursor='hand2', command=lambda x=q: self._rate(x)).pack()
            tk.Label(bf, text=interval_label(ni), font=('Cascadia Code', 9),
                     fg=T['text3'], bg=T['bg2']).pack(pady=(4, 0))

        # Skip
        tk.Button(card, text="Skip", font=('Segoe UI', 10), fg=T['text3'],
                  bg=T['bg2'], bd=0, activeforeground=T['text'],
                  activebackground=T['bg2'], cursor='hand2',
                  command=self._skip).pack(anchor='e', pady=(14, 0))

    def _rate(self, quality):
        tid, _ = self.review_queue[self.ci]
        d = self.progress['active'][tid]
        r, e, i = sm2(quality, d.get('repetitions', 0),
                       d.get('ease', 2.5), d.get('interval', 1))
        today = date.today()
        d.update({'repetitions': r, 'ease': e, 'interval': i,
                  'last_review': today.isoformat(),
                  'next_review': (today + timedelta(days=i)).isoformat()})
        save_progress(self.progress)
        self.ci += 1
        self.session_total += 1
        self._render_card()

    def _skip(self):
        self.ci += 1
        self._render_card()

    def _load_more(self):
        """Pull next batch: remaining due cards first, then upcoming (early review)."""
        batch = []
        # First pull any remaining due cards beyond the initial cap
        if self.extra_due:
            batch = self.extra_due[:self.DAILY_CAP]
            self.extra_due = self.extra_due[self.DAILY_CAP:]
        # If still room, pull upcoming cards (reviewing ahead of schedule)
        if len(batch) < self.DAILY_CAP and self.upcoming_cards:
            need = self.DAILY_CAP - len(batch)
            batch += self.upcoming_cards[:need]
            self.upcoming_cards = self.upcoming_cards[need:]

        self.review_queue = batch
        self.ci = 0
        if not self.review_queue:
            messagebox.showinfo("Review", "No more cards available to review.")
            return
        self._render_card()

    def _render_done(self):
        self._clear()
        c = tk.Frame(self.main, bg=T['bg'])
        c.place(relx=0.5, rely=0.4, anchor='center')

        tk.Label(c, text="Session Complete", font=('Segoe UI', 22, 'bold'),
                 fg=T['green'], bg=T['bg']).pack(pady=(0, 8))

        reviewed = self.session_total
        tk.Label(c, text=f"You reviewed {reviewed} card{'s' if reviewed != 1 else ''} today.",
                 font=('Segoe UI', 13), fg=T['text'], bg=T['bg']).pack(pady=(0, 12))

        # Show what's available for extra review
        extra_due = len(self.extra_due)
        upcoming = len(self.upcoming_cards)
        available = extra_due + upcoming

        if available > 0:
            parts = []
            if extra_due:
                parts.append(f"{extra_due} still due")
            if upcoming:
                parts.append(f"{upcoming} upcoming")
            desc = " + ".join(parts)

            tk.Label(c, text=f"{desc} — review more to get ahead",
                     font=('Segoe UI', 11), fg=T['text3'],
                     bg=T['bg']).pack(pady=(0, 24))

            btn_row = tk.Frame(c, bg=T['bg'])
            btn_row.pack(pady=(0, 12))

            tk.Button(btn_row, text=f"Review More ({min(self.DAILY_CAP, available)})",
                      font=('Segoe UI', 12, 'bold'), fg=T['bg'], bg=T['blue'],
                      activebackground='#4a90d9', bd=0, padx=24, pady=10,
                      cursor='hand2', command=self._load_more).pack(side='left', padx=(0, 12))

            tk.Button(btn_row, text="Done for Today",
                      font=('Segoe UI', 12), fg=T['text2'], bg=T['bg3'],
                      activebackground=T['bg4'], bd=0, padx=24, pady=10,
                      cursor='hand2', command=self._go_dashboard).pack(side='left')
        else:
            tk.Label(c, text="No more cards available — fully caught up!",
                     font=('Segoe UI', 11), fg=T['text3'],
                     bg=T['bg']).pack(pady=(0, 24))
            tk.Button(c, text="Back to Dashboard", font=('Segoe UI', 13, 'bold'),
                      fg=T['bg'], bg=T['green'], activebackground='#3ec96f',
                      bd=0, padx=28, pady=10, cursor='hand2',
                      command=self._go_dashboard).pack()


# ── Entry ──────────────────────────────────────────────────────────────────
def main():
    root = tk.Tk()
    try:
        root.update()
        hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, 20, ctypes.byref(ctypes.c_int(1)), ctypes.sizeof(ctypes.c_int))
    except Exception:
        pass
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Melvin Steals Sr. – Legend of Soul & Gospel",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Raleway:wght@300;400;500;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&display=swap');

/* ─── Root palette ──────────────────────────────────────────── */
:root {
    --gold:    #C9A84C;
    --gold2:   #E8C96C;
    --deep:    #0D0A06;
    --warm:    #1A1208;
    --cream:   #F5EDD6;
    --muted:   #9A8A6A;
    --accent:  #8B2020;
}

/* ─── Base reset ────────────────────────────────────────────── */
html, body, [data-testid="stApp"] {
    background: var(--deep) !important;
    color: var(--cream) !important;
}

/* ─── Sidebar ───────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #120E07 0%, #0D0A06 100%) !important;
    border-right: 1px solid rgba(201,168,76,0.25) !important;
}
[data-testid="stSidebar"] * { color: var(--cream) !important; }
[data-testid="stSidebar"] .stRadio label {
    font-family: 'Raleway', sans-serif !important;
    font-weight: 500 !important;
    letter-spacing: 0.08em !important;
    font-size: 0.85rem !important;
    text-transform: uppercase !important;
}

/* ─── Main container ────────────────────────────────────────── */
.main .block-container {
    padding: 1.5rem 3rem 4rem !important;
    max-width: 1100px !important;
}

/* ─── Typography ────────────────────────────────────────────── */
h1, h2, h3, h4 {
    font-family: 'Playfair Display', serif !important;
    color: var(--gold) !important;
}
p, li, label, span, div {
    font-family: 'Raleway', sans-serif !important;
}

/* ─── Gold divider ──────────────────────────────────────────── */
.gold-hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 2rem 0;
}

/* ─── Hero banner ───────────────────────────────────────────── */
.hero-banner {
    background: linear-gradient(135deg, #1A1208 0%, #2A1F0A 50%, #0D0A06 100%);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 4px;
    padding: 3.5rem 3rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
}
.hero-banner::before {
    content: '𝄞';
    position: absolute;
    font-size: 18rem;
    color: rgba(201,168,76,0.04);
    top: -3rem;
    right: -2rem;
    line-height: 1;
}
.hero-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 3.5rem !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    line-height: 1.1 !important;
    margin-bottom: 0.5rem !important;
    text-shadow: 0 2px 20px rgba(201,168,76,0.3);
}
.hero-subtitle {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.4rem !important;
    font-style: italic !important;
    color: var(--cream) !important;
    opacity: 0.85 !important;
    letter-spacing: 0.05em !important;
}
.hero-badge {
    display: inline-block;
    background: var(--accent);
    color: var(--cream) !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
    padding: 0.35rem 1rem !important;
    border-radius: 2px;
    margin-bottom: 1.2rem;
}

/* ─── Stat boxes ────────────────────────────────────────────── */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}
.stat-box {
    background: rgba(201,168,76,0.07);
    border: 1px solid rgba(201,168,76,0.2);
    border-radius: 4px;
    padding: 1.5rem 1rem;
    text-align: center;
}
.stat-number {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.4rem !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    display: block;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.stat-label {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    color: var(--muted) !important;
}

/* ─── Quote pull ────────────────────────────────────────────── */
.pull-quote {
    border-left: 3px solid var(--gold);
    padding: 1.2rem 1.8rem;
    background: rgba(201,168,76,0.05);
    margin: 2rem 0;
    border-radius: 0 4px 4px 0;
}
.pull-quote p {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.3rem !important;
    font-style: italic !important;
    color: var(--cream) !important;
    margin: 0 !important;
}

/* ─── Cards ─────────────────────────────────────────────────── */
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(201,168,76,0.15);
    border-radius: 4px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
}
.card-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.2rem !important;
    color: var(--gold) !important;
    margin-bottom: 0.6rem !important;
}

/* ─── Timeline ──────────────────────────────────────────────── */
.timeline-item {
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2rem;
    align-items: flex-start;
}
.timeline-year {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.5rem !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
    min-width: 70px;
    text-align: right;
    padding-top: 0.15rem;
}
.timeline-dot {
    width: 12px;
    height: 12px;
    background: var(--gold);
    border-radius: 50%;
    margin-top: 0.45rem;
    flex-shrink: 0;
    position: relative;
}
.timeline-dot::after {
    content: '';
    position: absolute;
    top: 12px;
    left: 5px;
    width: 2px;
    height: 60px;
    background: linear-gradient(to bottom, rgba(201,168,76,0.4), transparent);
}
.timeline-content h4 {
    font-family: 'Playfair Display', serif !important;
    color: var(--cream) !important;
    font-size: 1.05rem !important;
    margin-bottom: 0.3rem !important;
}
.timeline-content p {
    color: rgba(245,237,214,0.75) !important;
    font-size: 0.9rem !important;
    margin: 0 !important;
    line-height: 1.6 !important;
}

/* ─── Purchase card ─────────────────────────────────────────── */
.purchase-card {
    background: linear-gradient(135deg, #1A1208, #221808);
    border: 1px solid var(--gold);
    border-radius: 6px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 8px 40px rgba(201,168,76,0.12);
}
.price-tag {
    font-family: 'Playfair Display', serif !important;
    font-size: 3rem !important;
    font-weight: 900 !important;
    color: var(--gold) !important;
}

/* ─── Buttons ───────────────────────────────────────────────── */
.stButton > button {
    background: linear-gradient(135deg, var(--gold), var(--gold2)) !important;
    color: var(--deep) !important;
    font-family: 'Raleway', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    font-size: 0.82rem !important;
    border: none !important;
    border-radius: 2px !important;
    padding: 0.65rem 2rem !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    box-shadow: 0 4px 20px rgba(201,168,76,0.4) !important;
}

/* ─── Section headers ───────────────────────────────────────── */
.section-eyebrow {
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.68rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.25em !important;
    text-transform: uppercase !important;
    color: var(--gold) !important;
    margin-bottom: 0.4rem !important;
}
.section-heading {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.4rem !important;
    font-weight: 900 !important;
    color: var(--cream) !important;
    margin-bottom: 1.2rem !important;
    line-height: 1.2 !important;
}

/* ─── Contact form inputs ───────────────────────────────────── */
.stTextInput input, .stTextArea textarea, .stSelectbox select {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(201,168,76,0.3) !important;
    color: var(--cream) !important;
    border-radius: 2px !important;
    font-family: 'Raleway', sans-serif !important;
}

/* ─── Image captions ────────────────────────────────────────── */
.img-caption {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 0.85rem !important;
    font-style: italic !important;
    color: var(--muted) !important;
    text-align: center !important;
    margin-top: 0.4rem !important;
}

/* ─── Footer ────────────────────────────────────────────────── */
.site-footer {
    border-top: 1px solid rgba(201,168,76,0.2);
    padding-top: 2rem;
    margin-top: 4rem;
    text-align: center;
}
.site-footer p {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 0.9rem !important;
    color: var(--muted) !important;
    font-style: italic !important;
}

/* ─── Scrollbar ─────────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--deep); }
::-webkit-scrollbar-thumb { background: rgba(201,168,76,0.35); border-radius: 3px; }

/* ─── Success / info boxes ──────────────────────────────────── */
.stSuccess, .stInfo {
    border-radius: 2px !important;
    font-family: 'Raleway', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.5rem 0 1rem;'>
        <div style='font-family:"Playfair Display",serif; font-size:1.35rem;
                    color:#C9A84C; font-weight:900; line-height:1.2;'>
            MELVIN<br>STEALS SR.
        </div>
        <div style='font-family:"Cormorant Garamond",serif; font-size:0.8rem;
                    color:#9A8A6A; font-style:italic; margin-top:0.3rem;'>
            Songwriter · Educator · Minister
        </div>
        <hr style='border:none; height:1px;
                   background:linear-gradient(90deg,transparent,#C9A84C,transparent);
                   margin:1rem 0;'>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        [
            "🏠  Home",
            "👤  About Melvin",
            "🎵  With You Jesus — Purchase",
            "📖  Story of With You Jesus",
            "🎼  Legacy & Discography",
            "✉️  Contact & Booking",
        ],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div style='margin-top:2rem; padding:1rem; border:1px solid rgba(201,168,76,0.15);
                border-radius:4px; text-align:center;'>
        <div style='font-family:"Raleway",sans-serif; font-size:0.65rem;
                    letter-spacing:0.2em; text-transform:uppercase; color:#9A8A6A;'>
            Grammy Award Winner
        </div>
        <div style='font-family:"Playfair Display",serif; font-size:1rem;
                    color:#C9A84C; margin-top:0.3rem;'>
            Best Dance Recording
        </div>
        <div style='font-family:"Cormorant Garamond",serif; font-size:0.78rem;
                    font-style:italic; color:rgba(245,237,214,0.6); margin-top:0.1rem;'>
            2021 — "10%" · Kaytranada feat. Kali Uchis
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Pages ─────────────────────────────────────────────────────────────────────

# ════════════════════════════ HOME ════════════════════════════════════════════
if "Home" in page:
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">Aliquippa, Pennsylvania · Est. 1942</div>
        <div class="hero-title">Melvin Steals Sr.</div>
        <div class="hero-subtitle">The man who made the world fall in love</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <p class="section-eyebrow">Welcome</p>
        <p class="section-heading">A Voice Behind<br>the Classics</p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style='font-family:"Raleway",sans-serif; font-size:1.05rem;
                  color:rgba(245,237,214,0.88); line-height:1.8;'>
        Few songwriters can claim a catalog that spans the golden age of Philadelphia Soul
        to a Grammy Award–winning 21st-century dance track. Melvin Steals Sr. is one of them.
        </p>
        <p style='font-family:"Raleway",sans-serif; font-size:1.05rem;
                  color:rgba(245,237,214,0.88); line-height:1.8; margin-top:1rem;'>
        Born and raised in <strong style="color:#C9A84C;">Aliquippa, Pennsylvania</strong>,
        Melvin and his twin brother Mervin — known in the industry as
        <em style="color:#C9A84C;">Mystro &amp; Lyric</em> — wrote songs that became the
        soundtrack to a generation. Their most famous composition,
        <strong style="color:#C9A84C;">"Could It Be I'm Falling in Love"</strong> by
        The Spinners, reached #1 on the R&amp;B chart, #4 on the Billboard Hot 100, and
        sold over <strong style="color:#C9A84C;">one million copies</strong>.
        </p>
        <p style='font-family:"Raleway",sans-serif; font-size:1.05rem;
                  color:rgba(245,237,214,0.88); line-height:1.8; margin-top:1rem;'>
        Now, Melvin channels that same profound gift for melody and meaning into his
        heartfelt gospel single,
        <strong style="color:#C9A84C;">"With You Jesus"</strong> — a testament
        to faith, resilience, and the power of God's grace.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        # Photo placeholder with graceful fallback
        try:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/400px-Placeholder_view_vector.svg.png",
                use_container_width=True,
            )
        except Exception:
            pass
        st.markdown("""
        <div style='background:rgba(201,168,76,0.07); border:1px solid rgba(201,168,76,0.2);
                    border-radius:4px; padding:1.5rem; text-align:center;'>
            <div style='font-family:"Playfair Display",serif; font-size:3rem;
                        color:#C9A84C; line-height:1;'>♪</div>
            <div style='font-family:"Cormorant Garamond",serif; font-style:italic;
                        color:rgba(245,237,214,0.7); font-size:0.9rem; margin-top:0.5rem;'>
                Melvin Steals Sr.<br><span style='color:#C9A84C;'>Songwriter · Educator · Minister</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stat-grid">
        <div class="stat-box">
            <span class="stat-number">100+</span>
            <span class="stat-label">Songs Written &amp; Recorded</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">47</span>
            <span class="stat-label">Songs Still Played Worldwide</span>
        </div>
        <div class="stat-box">
            <span class="stat-number">4M+</span>
            <span class="stat-label">Radio Spins — "Could It Be"</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    # Featured artists
    st.markdown("""
    <p class="section-eyebrow">Recorded by Legends</p>
    <h3 style='font-family:"Playfair Display",serif; color:#cream; font-size:1.5rem;
               margin-bottom:1.2rem;'>Artists Who Recorded Steals Brothers Classics</h3>
    """, unsafe_allow_html=True)

    artists = [
        ("The Spinners", "Could It Be I'm Falling in Love"),
        ("Gloria Gaynor", "Honey Bee"),
        ("Archie Bell & The Drells", "Go For What You Know"),
        ("The Trammps", "Trusting Heart"),
        ("Blue Magic", "Steals Brothers Composition"),
        ("Harold Melvin & The Blue Notes", "Steals Brothers Composition"),
        ("Donnie Osmond", "Could It Be I'm Falling in Love (cover)"),
        ("Regina Belle", "Could It Be I'm Falling in Love (cover)"),
        ("A$AP Rocky", "Back Home (sample)"),
        ("Mary J. Blige", "Treat 'Em Right (sample)"),
        ("Kaytranada feat. Kali Uchis", "10% — 2021 Grammy Winner"),
        ("The Impressions", "Steals Brothers Composition"),
    ]

    cols = st.columns(3)
    for i, (artist, song) in enumerate(artists):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card" style="padding:1.1rem;">
                <div class="card-title" style="font-size:0.95rem;">{artist}</div>
                <div style='font-family:"Cormorant Garamond",serif; font-style:italic;
                            font-size:0.83rem; color:rgba(245,237,214,0.6);'>{song}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved · Aliquippa, Pennsylvania</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════ ABOUT ═══════════════════════════════════════════
elif "About" in page:
    st.markdown("""
    <p class="section-eyebrow">Biography</p>
    <h1 style='font-family:"Playfair Display",serif; font-size:3rem;
               color:#C9A84C; margin-bottom:0.3rem;'>About Melvin Steals Sr.</h1>
    <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
              color:rgba(245,237,214,0.7); font-size:1.1rem; margin-bottom:2rem;'>
        Songwriter · Educator · Minister · Grammy Award Winner
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="pull-quote">
            <p>"Could It Be I'm Falling in Love was inspired by my childhood sweetheart
            Adrena, whom I dated as a teenager — and later married."</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C;'>Early Life in Aliquippa</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        Melvin Steals Sr. was born and raised in Aliquippa, Pennsylvania — a Beaver County
        town on the Ohio River that would prove far more than its steel-mill reputation suggested.
        Alongside his twin brother Mervin, Melvin grew up steeped in music, nurturing a gift
        for words and melody that would one day reach millions of ears worldwide.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        After graduating high school in 1964, the twins enrolled at
        <strong style="color:#C9A84C;">Cheyney State College</strong> — America's oldest
        Historically Black College/University, located just outside Philadelphia.
        It was there they met Eddie Holman, forged lifelong friendships, and began rubbing
        shoulders with the Philadelphia music world that would soon make them legends.
        </p>

        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; margin-top:2rem;'>Breaking Into Philadelphia Soul</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        Kenny Gamble and Leon Huff — the architects of the Philadelphia Sound — held weekly
        auditions for aspiring songwriters in the early 1970s. Two financially strapped
        22-year-old twins from Beaver County walked through that door and never looked back.
        Gamble and Huff were immediately impressed and put them to work writing songs for
        <strong style="color:#C9A84C;">Archie Bell &amp; The Drells</strong>.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        In the studio, their roles were perfectly complementary: Melvin was the wordsmith —
        known as <em style="color:#C9A84C;">"Lyric"</em> — while Mervin crafted the melodies
        on piano under the alias <em style="color:#C9A84C;">"Mystro."</em> Together, as
        <strong style="color:#C9A84C;">Mystro &amp; Lyric</strong>, they became one of
        the most prolific songwriting duos of the Philadelphia Soul era.
        </p>

        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; margin-top:2rem;'>Teacher, Father &amp; Man of Faith</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        Even at the height of his songwriting success, Melvin never forgot his community.
        He returned to Aliquippa and taught in the local school system — a beloved educator
        remembered warmly by generations of students who had no idea their teacher's songs
        were on the radio and in record stores across the country.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85; color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        Guided by deep faith, Melvin eventually turned his songwriting gifts toward gospel
        music. His song <strong style="color:#C9A84C;">"With You Jesus"</strong> represents
        the full arc of his journey — a man who wrote the soundtrack to falling in love, now
        writing music about the deepest love of all.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:rgba(201,168,76,0.07); border:1px solid rgba(201,168,76,0.2);
                    border-radius:4px; padding:2rem; text-align:center; margin-bottom:1.5rem;'>
            <div style='font-family:"Playfair Display",serif; font-size:5rem;
                        color:#C9A84C; line-height:1;'>♫</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.3rem;
                        color:#C9A84C; margin-top:1rem;'>Melvin Steals Sr.</div>
            <div style='font-family:"Cormorant Garamond",serif; font-style:italic;
                        color:rgba(245,237,214,0.65); font-size:0.85rem; margin-top:0.3rem;'>
                "Lyric" of Mystro &amp; Lyric
            </div>
            <div style='border-top:1px solid rgba(201,168,76,0.2); margin-top:1.2rem;
                        padding-top:1.2rem;'>
                <div style='font-family:"Raleway",sans-serif; font-size:0.7rem;
                            letter-spacing:0.18em; text-transform:uppercase; color:#9A8A6A;'>
                    Born &amp; Raised</div>
                <div style='font-family:"Raleway",sans-serif; font-size:0.9rem;
                            color:rgba(245,237,214,0.85); margin-top:0.2rem;'>
                    Aliquippa, Pennsylvania</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Quick facts
        facts = [
            ("🏆", "Grammy Award Winner", "2021 Best Dance Recording"),
            ("📚", "Educator", "Taught in Aliquippa Schools"),
            ("✍️", "Wordsmith", "100+ Recorded Compositions"),
            ("❤️", "Love Story", "Married childhood sweetheart Adrena"),
            ("🎓", "Cheyney State College", "America's Oldest HBCU"),
            ("🙏", "Minister", "Gospel songwriter & minister of faith"),
        ]
        for icon, title, sub in facts:
            st.markdown(f"""
            <div class="card" style="padding:0.85rem 1.1rem; margin-bottom:0.6rem;">
                <div style='display:flex; align-items:center; gap:0.75rem;'>
                    <span style='font-size:1.2rem;'>{icon}</span>
                    <div>
                        <div style='font-family:"Raleway",sans-serif; font-size:0.82rem;
                                    font-weight:700; color:rgba(245,237,214,0.9);'>{title}</div>
                        <div style='font-family:"Cormorant Garamond",serif; font-size:0.78rem;
                                    font-style:italic; color:#9A8A6A;'>{sub}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════ PURCHASE ════════════════════════════════════════
elif "Purchase" in page:
    st.markdown("""
    <p class="section-eyebrow">New Release</p>
    <h1 style='font-family:"Playfair Display",serif; font-size:3rem;
               color:#C9A84C; margin-bottom:0.3rem;'>With You Jesus</h1>
    <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
              color:rgba(245,237,214,0.7); font-size:1.1rem; margin-bottom:2rem;'>
        The new gospel single by Melvin Steals Sr.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        # Album art placeholder
        st.markdown("""
        <div style='background:linear-gradient(135deg,#1A1208,#2E1F06,#0D0A06);
                    border:1px solid rgba(201,168,76,0.4); border-radius:6px;
                    aspect-ratio:1; display:flex; flex-direction:column;
                    align-items:center; justify-content:center; text-align:center;
                    padding:2rem; margin-bottom:1rem; box-shadow:0 12px 50px rgba(201,168,76,0.15);'>
            <div style='font-size:5rem; line-height:1; margin-bottom:1rem;'>✝</div>
            <div style='font-family:"Playfair Display",serif; font-size:2rem;
                        font-weight:900; color:#C9A84C; line-height:1.15;'>
                With You<br>Jesus
            </div>
            <div style='font-family:"Cormorant Garamond",serif; font-size:0.95rem;
                        font-style:italic; color:rgba(245,237,214,0.6); margin-top:0.7rem;'>
                Melvin Steals Sr.
            </div>
            <div style='margin-top:1.5rem; padding:0.4rem 1rem; border:1px solid rgba(201,168,76,0.4);
                        border-radius:20px; font-family:"Raleway",sans-serif; font-size:0.7rem;
                        font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:#C9A84C;'>
                Gospel Single
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
                  color:#9A8A6A; font-size:0.82rem; text-align:center;'>
            Cover artwork — "With You Jesus" single
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="purchase-card">
            <div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                        letter-spacing:0.25em; text-transform:uppercase; color:#9A8A6A;
                        margin-bottom:0.5rem;'>Digital Download</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.8rem;
                        font-weight:900; color:#C9A84C; margin-bottom:0.3rem;'>
                "With You Jesus"
            </div>
            <div style='font-family:"Cormorant Garamond",serif; font-size:1rem;
                        font-style:italic; color:rgba(245,237,214,0.65); margin-bottom:1.5rem;'>
                by Melvin Steals Sr.
            </div>
            <div class="price-tag">$1.29</div>
            <div style='font-family:"Raleway",sans-serif; font-size:0.78rem;
                        color:#9A8A6A; margin-bottom:1.8rem;'>MP3 · High Quality · Instant Download</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🎵  Purchase & Download — $1.29", use_container_width=True):
            st.success("Thank you! You will receive a download link at your email shortly. God bless you! 🙏")

        st.markdown("<br>", unsafe_allow_html=True)

        # Streaming options
        st.markdown("""
        <div style='text-align:center; margin-bottom:1rem;'>
            <div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                        letter-spacing:0.2em; text-transform:uppercase; color:#9A8A6A;'>
                Also Available On
            </div>
        </div>
        """, unsafe_allow_html=True)

        platforms = [
            ("🎵", "Apple Music", "Stream on Apple Music"),
            ("🟢", "Spotify", "Stream on Spotify"),
            ("▶️", "YouTube Music", "Listen on YouTube"),
            ("📀", "Amazon Music", "Stream on Amazon"),
        ]
        for icon, name, label in platforms:
            st.markdown(f"""
            <div style='background:rgba(255,255,255,0.04); border:1px solid rgba(201,168,76,0.15);
                        border-radius:4px; padding:0.7rem 1.2rem; margin-bottom:0.5rem;
                        display:flex; align-items:center; gap:0.8rem; cursor:pointer;'>
                <span style='font-size:1.1rem;'>{icon}</span>
                <span style='font-family:"Raleway",sans-serif; font-size:0.88rem;
                             font-weight:600; color:rgba(245,237,214,0.85);'>{name}</span>
                <span style='font-family:"Raleway",sans-serif; font-size:0.75rem;
                             color:#9A8A6A; margin-left:auto;'>{label} →</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style='margin-top:1.5rem; padding:1rem; background:rgba(201,168,76,0.06);
                    border-radius:4px; border:1px solid rgba(201,168,76,0.12);'>
            <div style='font-family:"Raleway",sans-serif; font-size:0.72rem;
                        font-weight:700; letter-spacing:0.15em; text-transform:uppercase;
                        color:#C9A84C; margin-bottom:0.5rem;'>What You Get</div>
            <ul style='font-family:"Raleway",sans-serif; font-size:0.85rem;
                       color:rgba(245,237,214,0.8); list-style:none; padding:0; margin:0;'>
                <li style='padding:0.2rem 0;'>✓ High-quality MP3 (320kbps)</li>
                <li style='padding:0.2rem 0;'>✓ Instant digital delivery</li>
                <li style='padding:0.2rem 0;'>✓ Personal use license</li>
                <li style='padding:0.2rem 0;'>✓ Direct support to the artist</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    # Bulk / church licensing
    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif; color:#C9A84C;
               font-size:1.6rem; margin-bottom:1rem;'>Church &amp; Ministry Licensing</h3>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3, gap="medium")
    for col, title, price, desc in zip(
        [col_a, col_b, col_c],
        ["Personal", "Church / Small Ministry", "Large Organization"],
        ["$1.29", "$25", "$75"],
        [
            "Single download for personal listening and devotion.",
            "Licensed for use in worship services, bulletins & events (up to 200 members).",
            "Broadcast rights, large congregations, conference use.",
        ],
    ):
        with col:
            st.markdown(f"""
            <div class="card" style='text-align:center; padding:1.8rem;'>
                <div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                            letter-spacing:0.2em; text-transform:uppercase; color:#9A8A6A;
                            margin-bottom:0.5rem;'>{title}</div>
                <div style='font-family:"Playfair Display",serif; font-size:2.2rem;
                            font-weight:900; color:#C9A84C; margin-bottom:0.6rem;'>{price}</div>
                <div style='font-family:"Raleway",sans-serif; font-size:0.83rem;
                            color:rgba(245,237,214,0.72); line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved · For licensing inquiries, please use the Contact page.</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════ STORY OF WITH YOU JESUS ═════════════════════════
elif "Story" in page:
    st.markdown("""
    <p class="section-eyebrow">Behind the Music</p>
    <h1 style='font-family:"Playfair Display",serif; font-size:3rem;
               color:#C9A84C; margin-bottom:0.3rem;'>The Story of<br>"With You Jesus"</h1>
    <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
              color:rgba(245,237,214,0.7); font-size:1.1rem; margin-bottom:2rem;'>
        A songwriter's journey from Philadelphia Soul to Gospel grace
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="pull-quote">
        <p>"The same heart that wrote about falling in love with a person
        eventually found itself overwhelmed by a love far greater —
        the love of Jesus Christ."</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C;'>From Soul to Spirit</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        When Melvin Steals Sr. and his twin brother Mervin wrote
        <em style="color:#C9A84C;">"Could It Be I'm Falling in Love"</em>
        for The Spinners in 1972, they were drawing from a very personal well.
        The song was inspired by Melvin's real-life romance with Adrena, his childhood
        sweetheart. That authenticity — writing from the depths of lived experience —
        became the hallmark of everything Melvin created.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        Decades passed. The hits stacked up. The Grammy came. And through it all,
        Melvin's faith deepened. Having witnessed the transience of earthly fame and
        the enduring strength that faith provided through every season of life, he felt
        a growing call to use his pen not just to celebrate romantic love, but the
        transformative love he'd found in Jesus Christ.
        </p>

        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; margin-top:2rem;'>
            The Inspiration</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        <strong style="color:#C9A84C;">"With You Jesus"</strong> was born from a place of
        quiet reflection and profound gratitude. Melvin sat with the realization that
        across a lifetime of songwriting — love songs, soul anthems, tracks that became
        certified gold — the most important story he had yet to tell was the one about
        what carried him through it all.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        The song speaks to the peace that comes not from chart positions or radio spins,
        but from a personal relationship with God. Just as his secular work drew from the
        intimacy of his marriage to Adrena, this gospel piece draws from the intimacy of
        a spiritual life lived intentionally.
        </p>

        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; margin-top:2rem;'>
            A Legacy Completed</h3>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem;'>
        For Melvin, <em style="color:#C9A84C;">"With You Jesus"</em> is not a departure
        from his legacy — it is its fulfillment. The same craft that made "Could It Be
        I'm Falling in Love" one of the most enduring songs in R&amp;B history is present
        in every note: the hook, the heart, the honesty.
        </p>
        <p style='font-family:"Raleway",sans-serif; line-height:1.85;
                  color:rgba(245,237,214,0.88); font-size:0.97rem; margin-top:1rem;'>
        For those who grew up hearing "Could It Be" on the radio or at the school dance,
        this new song offers something just as true — a message that love, in its highest
        form, is always worth singing about.
        </p>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style='background:rgba(201,168,76,0.07); border:1px solid rgba(201,168,76,0.2);
                    border-radius:4px; padding:1.8rem; margin-bottom:1.5rem;'>
            <div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                        letter-spacing:0.2em; text-transform:uppercase; color:#9A8A6A;
                        margin-bottom:1rem;'>Song Themes</div>
        """, unsafe_allow_html=True)

        themes = [
            ("Faith", "Trust in God's constant presence"),
            ("Grace", "Finding peace through surrender"),
            ("Gratitude", "Thankfulness for a life well-lived"),
            ("Legacy", "Leaving a spiritual inheritance"),
            ("Love", "The highest love — divine and unconditional"),
        ]
        for theme, desc in themes:
            st.markdown(f"""
            <div style='border-left:2px solid #C9A84C; padding:0.6rem 1rem;
                        margin-bottom:0.8rem;'>
                <div style='font-family:"Playfair Display",serif; font-size:0.95rem;
                            color:#C9A84C; font-weight:700;'>{theme}</div>
                <div style='font-family:"Cormorant Garamond",serif; font-size:0.82rem;
                            font-style:italic; color:rgba(245,237,214,0.65);'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style='text-align:center; padding:2rem;'>
            <div style='font-size:2.5rem; margin-bottom:0.8rem;'>✝</div>
            <div style='font-family:"Playfair Display",serif; font-size:1.3rem;
                        color:#C9A84C; font-style:italic; line-height:1.4;'>
                "With You Jesus"
            </div>
            <div style='font-family:"Cormorant Garamond",serif; font-size:0.85rem;
                        color:rgba(245,237,214,0.6); margin-top:0.5rem; font-style:italic;'>
                Melvin Steals Sr.
            </div>
            <div style='margin-top:1.5rem; font-family:"Raleway",sans-serif; font-size:0.75rem;
                        color:#9A8A6A; letter-spacing:0.12em; text-transform:uppercase;'>
                Gospel Single — Available Now
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; font-size:1.6rem;
               margin-bottom:1.5rem;'>The Journey in His Own Words</h3>
    """, unsafe_allow_html=True)

    quotes = [
        ("On Writing", "When you write from truth, the song writes itself. I've always written from life."),
        ("On Faith", "Music can take you to the mountaintop, but only faith can keep you there."),
        ("On Legacy", "I want people to hear 'With You Jesus' fifty years from now the same way they still hear 'Could It Be' today."),
        ("On Aliquippa", "That town made me who I am. Everything I've written has Aliquippa in it, whether people know it or not."),
    ]
    cols = st.columns(2)
    for i, (label, quote) in enumerate(quotes):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="card" style='padding:1.6rem;'>
                <div style='font-family:"Raleway",sans-serif; font-size:0.65rem;
                            letter-spacing:0.2em; text-transform:uppercase;
                            color:#C9A84C; margin-bottom:0.6rem;'>{label}</div>
                <div style='font-family:"Cormorant Garamond",serif; font-size:1.1rem;
                            font-style:italic; color:rgba(245,237,214,0.88);
                            line-height:1.6;'>"{quote}"</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════ LEGACY & DISCOGRAPHY ════════════════════════════
elif "Legacy" in page:
    st.markdown("""
    <p class="section-eyebrow">The Catalog</p>
    <h1 style='font-family:"Playfair Display",serif; font-size:3rem;
               color:#C9A84C; margin-bottom:0.3rem;'>Legacy &amp; Discography</h1>
    <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
              color:rgba(245,237,214,0.7); font-size:1.1rem; margin-bottom:2rem;'>
        Five decades of music that shaped American soul, R&amp;B, and gospel
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    # Timeline
    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif; color:#C9A84C;
               font-size:1.8rem; margin-bottom:1.5rem;'>A Life in Music</h3>
    """, unsafe_allow_html=True)

    timeline = [
        ("1942", "Born in Aliquippa, PA", "Melvin and twin brother Mervin Steals are born and raised in Aliquippa, Pennsylvania — a Beaver County mill town along the Ohio River."),
        ("1964", "Cheyney State College", "The twins enroll at America's oldest HBCU just outside Philadelphia, where they meet future R&B star Eddie Holman and enter the orbit of the Philadelphia music world."),
        ("Early 70s", "Gamble & Huff Discovery", "As 22-year-old struggling songwriters, Melvin and Mervin audition for legendary producers Kenny Gamble and Leon Huff, who immediately put them to work."),
        ("1972", '"I\'m Not Strong Enough"', "The Steals Brothers record their first single as The Four Perfections. It becomes a collector's item on the UK Northern Soul circuit, with pristine copies selling for up to $1,000."),
        ("1972", "Atlantic Records & Thom Bell", "Thom Bell hears seven Steals Brothers songs on a scouting trip to Pittsburgh, agrees to find artists to record them, and one of them is destined for history."),
        ("Dec 1972", '"Could It Be I\'m Falling in Love"', "Released by The Spinners on Atlantic Records. Written by Melvin (Lyric) and Mervin (Mystro). Produced by Thom Bell at Sigma Sound Studios, Philadelphia."),
        ("1973", "Gold Certification", "\"Could It Be\" peaks at #1 R&B, #4 Billboard Hot 100, and sells over one million copies — achieving gold certification."),
        ("1974", '"Honey Bee" — Gloria Gaynor', "The Steals Brothers' composition becomes a successful single for future disco legend Gloria Gaynor."),
        ("70s–80s", "Prolific Catalog", "The twins write over 100 songs recorded by a roster including Blue Magic, Harold Melvin & The Blue Notes, The Trammps, Archie Bell, and O.C. Smith."),
        ("80s–90s", "Educator & Community", "Melvin serves as a beloved teacher in the Aliquippa school system, shaping generations of young people while continuing to write music."),
        ("2021", "Grammy Award Win", "Melvin and Mervin, alongside business partner McKinley Jackson (Marvin Gaye's musical director), receive Grammy Awards as co-writers of \"10%\" by Kaytranada featuring Kali Uchis — Best Dance Recording."),
        ("2020s", '"With You Jesus"', "Melvin releases his gospel single, channeling a lifetime of faith and musical mastery into a song of spiritual devotion."),
    ]

    for year, title, desc in timeline:
        st.markdown(f"""
        <div class="timeline-item">
            <div class="timeline-year">{year}</div>
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<hr class="gold-hr">', unsafe_allow_html=True)

    # Notable songs table
    st.markdown("""
    <h3 style='font-family:"Playfair Display",serif; color:#C9A84C;
               font-size:1.8rem; margin-bottom:1.5rem;'>Notable Compositions</h3>
    """, unsafe_allow_html=True)

    songs = [
        ("Could It Be I'm Falling in Love", "The Spinners", "1972", "#1 R&B · #4 Billboard · Gold"),
        ("Honey Bee", "Gloria Gaynor", "1974", "Top 40 Hit"),
        ("Trusting Heart", "The Trammps", "1970s", "Philly Soul Staple"),
        ("Go For What You Know", "Archie Bell & The Drells", "Early 70s", "B-Side to 'There's Gonna Be a Showdown'"),
        ("I'm Not Strong Enough", "The Four Perfections", "1972", "UK Northern Soul Classic · $1,000 Collector's Copy"),
        ("10% (co-write)", "Kaytranada ft. Kali Uchis", "2020", "Grammy Award — Best Dance Recording 2021"),
        ("Back Home (sample)", "A$AP Rocky", "2010s", "Hip-Hop Sample"),
        ("Treat 'Em Right (sample)", "Mary J. Blige", "1990s", "R&B/Hip-Hop Sample"),
        ("With You Jesus", "Melvin Steals Sr.", "2020s", "Gospel Single — Available Now"),
    ]

    header_cols = st.columns([3, 3, 1, 3])
    for col, label in zip(header_cols, ["Song", "Artist", "Year", "Notes"]):
        with col:
            st.markdown(f"""<div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                letter-spacing:0.18em; text-transform:uppercase; color:#C9A84C;
                padding-bottom:0.5rem; border-bottom:1px solid rgba(201,168,76,0.3);'>
                {label}</div>""", unsafe_allow_html=True)

    for song, artist, year, notes in songs:
        row_cols = st.columns([3, 3, 1, 3])
        for col, val, clr in zip(
            row_cols,
            [song, artist, year, notes],
            ["rgba(245,237,214,0.92)", "rgba(245,237,214,0.7)", "#C9A84C", "rgba(245,237,214,0.6)"],
        ):
            with col:
                st.markdown(f"""<div style='font-family:"Raleway",sans-serif; font-size:0.87rem;
                    color:{clr}; padding:0.6rem 0;
                    border-bottom:1px solid rgba(255,255,255,0.05);'>{val}</div>""",
                    unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════ CONTACT ═════════════════════════════════════════
elif "Contact" in page:
    st.markdown("""
    <p class="section-eyebrow">Get in Touch</p>
    <h1 style='font-family:"Playfair Display",serif; font-size:3rem;
               color:#C9A84C; margin-bottom:0.3rem;'>Contact &amp; Booking</h1>
    <p style='font-family:"Cormorant Garamond",serif; font-style:italic;
              color:rgba(245,237,214,0.7); font-size:1.1rem; margin-bottom:2rem;'>
        For bookings, licensing, media inquiries, and ministry partnerships
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        st.markdown("""
        <h3 style='font-family:"Playfair Display",serif; color:#C9A84C; margin-bottom:1rem;'>
            Send a Message</h3>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name *", placeholder="Your name")
        email = st.text_input("Email Address *", placeholder="your@email.com")
        subject = st.selectbox(
            "Subject *",
            [
                "Select a topic...",
                "Booking / Live Performance",
                "Song Licensing",
                "Media / Press Inquiry",
                "Ministry Partnership",
                "Purchase Support",
                "General Message",
            ],
        )
        message = st.text_area(
            "Your Message *",
            placeholder="Write your message here...",
            height=160,
        )

        col_btn, col_pad = st.columns([1, 3])
        with col_btn:
            if st.button("Send Message →", use_container_width=True):
                if name and email and message and subject != "Select a topic...":
                    st.success("✓ Message sent! We'll be in touch within 2–3 business days. God bless you!")
                else:
                    st.warning("Please fill in all required fields before sending.")

    with col2:
        st.markdown("""
        <div class="card" style='padding:2rem; margin-bottom:1.2rem;'>
            <div style='font-family:"Playfair Display",serif; font-size:1.2rem;
                        color:#C9A84C; margin-bottom:1.2rem;'>Contact Details</div>
        """, unsafe_allow_html=True)

        contact_items = [
            ("📍", "Location", "Aliquippa, Pennsylvania"),
            ("🎤", "Bookings", "Available for speaking engagements, gospel concerts & ministry events"),
            ("📜", "Licensing", "Song licensing for churches, media & commercial use"),
            ("📰", "Press", "Media kits and interviews available on request"),
        ]
        for icon, label, val in contact_items:
            st.markdown(f"""
            <div style='display:flex; gap:1rem; margin-bottom:1rem; align-items:flex-start;'>
                <span style='font-size:1.2rem; padding-top:0.1rem;'>{icon}</span>
                <div>
                    <div style='font-family:"Raleway",sans-serif; font-size:0.68rem;
                                letter-spacing:0.15em; text-transform:uppercase;
                                color:#9A8A6A;'>{label}</div>
                    <div style='font-family:"Raleway",sans-serif; font-size:0.87rem;
                                color:rgba(245,237,214,0.85); margin-top:0.2rem;
                                line-height:1.5;'>{val}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="card" style='padding:1.8rem; text-align:center;'>
            <div style='font-family:"Playfair Display",serif; font-size:1.1rem;
                        color:#C9A84C; margin-bottom:0.6rem;'>Speaking &amp; Ministry</div>
            <p style='font-family:"Raleway",sans-serif; font-size:0.85rem;
                      color:rgba(245,237,214,0.75); line-height:1.6; margin-bottom:1rem;'>
            Melvin is available to share his remarkable story — from the streets of Aliquippa
            to the top of the charts, and from the charts to the feet of Jesus.
            </p>
            <div style='font-family:"Cormorant Garamond",serif; font-style:italic;
                        color:#C9A84C; font-size:0.9rem;'>
                "Every song I ever wrote was practice for the most important one."
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="site-footer">
        <p>© 2025 Melvin Steals Sr. · All Rights Reserved · Aliquippa, Pennsylvania</p>
    </div>
    """, unsafe_allow_html=True)

from pathlib import Path

DASHBOARD = Path("dashboard.html")
MEN = Path("themes/men.html")


dashboard = DASHBOARD.read_text(encoding="utf-8")
men = MEN.read_text(encoding="utf-8")


if 'id="etagThemeBoard"' not in dashboard:
    dashboard_css = r'''

    <style id="etagTwoColorThemeStyle">

        #etagThemeBoard {
            margin-top: 26px;
            margin-bottom: 18px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }

        #etagThemeBoard h3 {
            margin: 0 0 6px;
            font-size: 17px;
        }

        #etagThemeBoard .theme-board-help {
            margin: 0 0 15px;
            color: #6b7280;
            font-size: 12px;
            line-height: 1.5;
        }

        #etagThemeBoard .theme-tabs {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px;
            margin-bottom: 12px;
        }

        #etagThemeBoard .theme-tab {
            border: 2px solid #e5e7eb;
            background: #ffffff;
            border-radius: 12px;
            padding: 10px 12px;
            font: inherit;
            font-size: 13px;
            font-weight: 700;
            color: #111827;
            cursor: pointer;
        }

        #etagThemeBoard .theme-tab.active {
            border-color: #111827;
            background: #f9fafb;
        }

        #etagThemeBoard .theme-color-board {
            position: relative;
            width: 100%;
            height: 210px;
            border-radius: 16px;
            overflow: hidden;
            cursor: crosshair;
            touch-action: none;
            background: hsl(140 100% 50%);
            box-shadow: inset 0 0 0 1px rgba(17,24,39,.08);
        }

        #etagThemeBoard .theme-color-white,
        #etagThemeBoard .theme-color-black {
            position: absolute;
            inset: 0;
            pointer-events: none;
        }

        #etagThemeBoard .theme-color-white {
            background: linear-gradient(to right, #fff 0%, rgba(255,255,255,0) 55%);
        }

        #etagThemeBoard .theme-color-black {
            background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,1) 100%);
        }

        #etagThemeBoard .theme-color-pointer {
            position: absolute;
            width: 20px;
            height: 20px;
            margin: -10px 0 0 -10px;
            border-radius: 50%;
            border: 3px solid #fff;
            box-shadow: 0 0 0 2px rgba(17,24,39,.45), 0 4px 12px rgba(0,0,0,.22);
            pointer-events: none;
        }

        #etagThemeBoard .theme-hue {
            width: 100%;
            height: 20px;
            margin-top: 10px;
            border-radius: 999px;
            background: linear-gradient(90deg,#ff0000 0%,#ffff00 16.66%,#00ff00 33.33%,#00ffff 50%,#0000ff 66.66%,#ff00ff 83.33%,#ff0000 100%);
            cursor: pointer;
            touch-action: none;
            position: relative;
        }

        #etagThemeBoard .theme-hue-pointer {
            position: absolute;
            top: 50%;
            width: 24px;
            height: 24px;
            margin: -12px 0 0 -12px;
            border-radius: 50%;
            border: 3px solid #fff;
            box-shadow: 0 0 0 2px rgba(17,24,39,.45), 0 3px 10px rgba(0,0,0,.18);
            pointer-events: none;
        }

        #etagThemeBoard .theme-value-row {
            display: grid;
            grid-template-columns: 1fr 86px;
            gap: 10px;
            align-items: center;
            margin-top: 12px;
        }

        #etagThemeBoard .theme-hex {
            width: 100%;
            padding: 12px 13px;
            border: 1px solid #d1d5db;
            border-radius: 11px;
            font: inherit;
            font-size: 14px;
            outline: none;
            text-transform: uppercase;
        }

        #etagThemeBoard .theme-preview-chip {
            height: 46px;
            border-radius: 11px;
            border: 1px solid #d1d5db;
            box-shadow: inset 0 0 0 1px rgba(255,255,255,.38);
        }

        #etagThemeBoard .theme-actions {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 12px;
        }

        @media (max-width: 600px) {
            #etagThemeBoard .theme-color-board {
                height: 190px;
            }
        }

    </style>
'''
    if "</head>" not in dashboard:
        raise RuntimeError("dashboard </head> not found")
    dashboard = dashboard.replace("</head>", dashboard_css + "\n</head>", 1)

    panel = r'''

                <div
                    id="etagThemeBoard"
                >

                    <h3>
                        Theme Appearance
                    </h3>

                    <p class="theme-board-help">
                        Choose your profile background and background glow.
                        Nothing else in the theme is recolored.
                    </p>

                    <div class="theme-tabs">
                        <button
                            id="etagThemeBackgroundTab"
                            class="theme-tab active"
                            type="button"
                        >
                            Background
                        </button>

                        <button
                            id="etagThemeGlowTab"
                            class="theme-tab"
                            type="button"
                        >
                            Background Glow
                        </button>
                    </div>

                    <div
                        id="etagThemeColorBoard"
                        class="theme-color-board"
                    >
                        <div class="theme-color-white"></div>
                        <div class="theme-color-black"></div>
                        <div
                            id="etagThemeColorPointer"
                            class="theme-color-pointer"
                        ></div>
                    </div>

                    <div
                        id="etagThemeHue"
                        class="theme-hue"
                    >
                        <div
                            id="etagThemeHuePointer"
                            class="theme-hue-pointer"
                        ></div>
                    </div>

                    <div class="theme-value-row">
                        <input
                            id="etagThemeHex"
                            class="theme-hex"
                            type="text"
                            maxlength="7"
                            value="#D3DBC8"
                            spellcheck="false"
                        >

                        <div
                            id="etagThemeChip"
                            class="theme-preview-chip"
                        ></div>
                    </div>

                    <div class="theme-actions">
                        <button
                            id="etagThemeSave"
                            class="button primary"
                            type="button"
                        >
                            Save Theme Colors
                        </button>

                        <button
                            id="etagThemeReset"
                            class="button secondary"
                            type="button"
                        >
                            Reset Colors
                        </button>
                    </div>

                </div>
'''
    marker = '                <div class="button-row">'
    if marker not in dashboard:
        raise RuntimeError("dashboard button row not found")
    dashboard = dashboard.replace(marker, panel + "\n" + marker, 1)

    dashboard_script = r'''

<script type="module">

    import { createClient }
    from "https://esm.sh/@supabase/supabase-js@2";

    const etagThemeSupabase = createClient(
        "https://zuptxhcjzhqynrquyray.supabase.co",
        "sb_publishable_1sa0MtE83MZXETR5JLakJA_fRVrjDJI"
    );

    const defaults = {
        background: "#D3DBC8",
        glow: "#FFFFFF"
    };

    let colors = { ...defaults };
    let mode = "background";
    let hue = 140;
    let saturation = .22;
    let lightness = .83;

    const board = document.getElementById("etagThemeColorBoard");
    const hueBar = document.getElementById("etagThemeHue");
    const pointer = document.getElementById("etagThemeColorPointer");
    const huePointer = document.getElementById("etagThemeHuePointer");
    const hex = document.getElementById("etagThemeHex");
    const chip = document.getElementById("etagThemeChip");
    const save = document.getElementById("etagThemeSave");
    const reset = document.getElementById("etagThemeReset");
    const backgroundTab = document.getElementById("etagThemeBackgroundTab");
    const glowTab = document.getElementById("etagThemeGlowTab");

    function rgbToHsl(r,g,b) {
        const max = Math.max(r,g,b);
        const min = Math.min(r,g,b);
        let h = 0;
        let s = 0;
        const l = (max + min) / 2;
        const d = max - min;
        if (d !== 0) {
            s = l > .5 ? d / (2 - max - min) : d / (max + min);
            switch (max) {
                case r: h = ((g-b)/d + (g < b ? 6 : 0)) / 6; break;
                case g: h = ((b-r)/d + 2) / 6; break;
                default: h = ((r-g)/d + 4) / 6; break;
            }
        }
        return { h: h * 360, s, l };
    }

    function hexToHsl(value) {
        const raw = String(value || "").replace("#", "");
        if (!/^[0-9a-fA-F]{6}$/.test(raw)) return null;
        return rgbToHsl(
            parseInt(raw.slice(0,2),16) / 255,
            parseInt(raw.slice(2,4),16) / 255,
            parseInt(raw.slice(4,6),16) / 255
        );
    }

    function hueToRgb(p,q,t) {
        if (t < 0) t += 1;
        if (t > 1) t -= 1;
        if (t < 1/6) return p + (q-p) * 6 * t;
        if (t < 1/2) return q;
        if (t < 2/3) return p + (q-p) * (2/3-t) * 6;
        return p;
    }

    function hslToHex(h,s,l) {
        h /= 360;
        let r,g,b;
        if (s === 0) {
            r = g = b = l;
        } else {
            const q = l < .5 ? l * (1+s) : l+s-l*s;
            const p = 2*l-q;
            r = hueToRgb(p,q,h+1/3);
            g = hueToRgb(p,q,h);
            b = hueToRgb(p,q,h-1/3);
        }
        const hexPart = value => Math.round(value*255).toString(16).padStart(2,"0");
        return `#${hexPart(r)}${hexPart(g)}${hexPart(b)}`.toUpperCase();
    }

    function modeColor() {
        return colors[mode];
    }

    function validHex(value) {
        return /^#[0-9A-F]{6}$/i.test(String(value || "").trim());
    }

    function updateBoard() {
        const hsl = hexToHsl(modeColor());
        if (hsl) {
            hue = hsl.h;
            saturation = hsl.s;
            lightness = hsl.l;
        }

        board.style.background = `hsl(${hue} 100% 50%)`;
        const rect = board.getBoundingClientRect();
        if (rect.width && rect.height) {
            pointer.style.left = `${saturation * rect.width}px`;
            pointer.style.top = `${(1-lightness) * rect.height}px`;
        }
        const hueWidth = hueBar.clientWidth;
        if (hueWidth) {
            huePointer.style.left = `${(hue / 360) * hueWidth}px`;
        }
        hex.value = modeColor();
        chip.style.background = modeColor();
        backgroundTab.classList.toggle("active", mode === "background");
        glowTab.classList.toggle("active", mode === "glow");
    }

    function sendPreview() {
        const frame = document.getElementById("themePreviewFrame");
        if (!frame?.contentWindow) return;
        frame.contentWindow.postMessage(
            { type: "etag-theme-colors", colors: { ...colors } },
            window.location.origin
        );
    }

    function updateBoardColor(clientX,clientY) {
        const rect = board.getBoundingClientRect();
        if (!rect.width || !rect.height) return;
        saturation = Math.max(0,Math.min(1,(clientX-rect.left)/rect.width));
        lightness = 1-Math.max(0,Math.min(1,(clientY-rect.top)/rect.height));
        colors[mode] = hslToHex(hue,saturation,lightness);
        updateBoard();
        sendPreview();
    }

    function updateHue(clientX) {
        const rect = hueBar.getBoundingClientRect();
        if (!rect.width) return;
        hue = Math.max(0,Math.min(360,((clientX-rect.left)/rect.width)*360));
        colors[mode] = hslToHex(hue,saturation,lightness);
        updateBoard();
        sendPreview();
    }

    board.addEventListener("pointerdown", event => {
        board.setPointerCapture?.(event.pointerId);
        updateBoardColor(event.clientX,event.clientY);
    });

    board.addEventListener("pointermove", event => {
        if (event.buttons) updateBoardColor(event.clientX,event.clientY);
    });

    hueBar.addEventListener("pointerdown", event => {
        hueBar.setPointerCapture?.(event.pointerId);
        updateHue(event.clientX);
    });

    hueBar.addEventListener("pointermove", event => {
        if (event.buttons) updateHue(event.clientX);
    });

    function chooseMode(next) {
        mode = next;
        updateBoard();
    }

    backgroundTab.addEventListener("click", () => chooseMode("background"));
    glowTab.addEventListener("click", () => chooseMode("glow"));

    hex.addEventListener("change", () => {
        const value = String(hex.value || "").trim().toUpperCase();
        if (!validHex(value)) {
            updateBoard();
            return;
        }
        colors[mode] = value;
        updateBoard();
        sendPreview();
    });

    async function loadSavedTheme() {
        try {
            const { data } = await etagThemeSupabase.auth.getSession();
            const user = data?.session?.user;
            if (!user) return;
            const result = await etagThemeSupabase
                .from("profiles")
                .select("theme_colors")
                .eq("id",user.id)
                .maybeSingle();
            if (result.data?.theme_colors && typeof result.data.theme_colors === "object") {
                colors = { ...defaults, ...result.data.theme_colors };
            }
            updateBoard();
            sendPreview();
        } catch (error) {
            console.error("Theme color load error:",error);
        }
    }

    save.addEventListener("click", async () => {
        save.disabled = true;
        save.textContent = "Saving...";
        try {
            const { data } = await etagThemeSupabase.auth.getSession();
            const user = data?.session?.user;
            if (!user) throw new Error("Your login session has expired.");
            const result = await etagThemeSupabase
                .from("profiles")
                .update({
                    theme_colors: {
                        background: colors.background,
                        glow: colors.glow
                    },
                    updated_at: new Date().toISOString()
                })
                .eq("id",user.id);
            if (result.error) throw result.error;
            save.textContent = "Saved";
            const message = document.getElementById("message");
            if (message) {
                message.textContent = "Theme colors saved successfully.";
                message.className = "message show success";
            }
            setTimeout(() => { save.textContent = "Save Theme Colors"; },1200);
        } catch (error) {
            const message = document.getElementById("message");
            if (message) {
                message.textContent = error.message || "Failed to save theme colors.";
                message.className = "message show error";
            }
            save.textContent = "Save Theme Colors";
        } finally {
            save.disabled = false;
        }
    });

    reset.addEventListener("click", () => {
        colors = { ...defaults };
        updateBoard();
        sendPreview();
    });

    window.addEventListener("message", event => {
        if (event.origin !== window.location.origin) return;
        if (event.data?.type === "etag-men-preview-ready") sendPreview();
    });

    loadSavedTheme();

</script>
'''
    dashboard = dashboard.replace("</body>", dashboard_script + "\n</body>", 1)


if 'id="etagThemeRuntime"' not in men:
    men_css = r'''

    <style id="etagThemeRuntime">

        :root {
            --etag-theme-background: #D3DBC8;
            --etag-theme-glow: #FFFFFF;
        }

        body {
            background:
                radial-gradient(
                    ellipse at 70% 18%,
                    color-mix(in srgb, var(--etag-theme-glow) 92%, transparent) 0%,
                    color-mix(in srgb, var(--etag-theme-glow) 45%, transparent) 27%,
                    transparent 57%
                ),
                radial-gradient(
                    ellipse at 15% 75%,
                    color-mix(in srgb, var(--etag-theme-background) 56%, transparent) 0%,
                    color-mix(in srgb, var(--etag-theme-background) 34%, transparent) 35%,
                    transparent 70%
                ),
                linear-gradient(
                    135deg,
                    color-mix(in srgb, var(--etag-theme-background) 72%, #ffffff) 0%,
                    color-mix(in srgb, var(--etag-theme-background) 88%, #ffffff) 38%,
                    color-mix(in srgb, var(--etag-theme-background) 64%, #ffffff) 68%,
                    color-mix(in srgb, var(--etag-theme-background) 78%, #ffffff) 100%
                );
        }

        body::before {
            background:
                radial-gradient(
                    ellipse at 72% 24%,
                    color-mix(in srgb, var(--etag-theme-glow) 42%, transparent),
                    transparent 32%
                ),
                radial-gradient(
                    ellipse at 20% 15%,
                    rgba(255,255,255,.26),
                    transparent 22%
                );
        }

    </style>
'''
    if "</head>" not in men:
        raise RuntimeError("men </head> not found")
    men = men.replace("</head>", men_css + "\n</head>", 1)

    men_script = r'''

<script type="module" id="etagThemeRuntimeScript">

    import { createClient }
    from "https://esm.sh/@supabase/supabase-js@2";

    const themeSupabase = createClient(
        "https://zuptxhcjzhqynrquyray.supabase.co",
        "sb_publishable_1sa0MtE83MZXETR5JLakJA_fRVrjDJI"
    );

    const defaults = {
        background: "#D3DBC8",
        glow: "#FFFFFF"
    };

    function applyTheme(colors) {
        const next = {
            ...defaults,
            ...(colors && typeof colors === "object" ? colors : {})
        };
        const background = /^#[0-9A-F]{6}$/i.test(String(next.background || ""))
            ? String(next.background).toUpperCase()
            : defaults.background;
        const glow = /^#[0-9A-F]{6}$/i.test(String(next.glow || ""))
            ? String(next.glow).toUpperCase()
            : defaults.glow;
        document.documentElement.style.setProperty("--etag-theme-background",background);
        document.documentElement.style.setProperty("--etag-theme-glow",glow);
    }

    window.addEventListener("message", event => {
        if (event.origin !== window.location.origin) return;
        if (event.data?.type === "etag-theme-colors") {
            applyTheme(event.data.colors);
        }
    });

    const params = new URLSearchParams(window.location.search);
    const preview = params.get("preview") === "1";

    if (preview) {
        window.parent.postMessage(
            { type: "etag-men-preview-ready" },
            window.location.origin
        );
    } else {
        (async () => {
            try {
                const tagCode = params.get("tag")?.trim().toUpperCase();
                if (!tagCode) return;
                const tagResult = await themeSupabase
                    .from("nfc_tags")
                    .select("owner_id,active")
                    .eq("tag_code",tagCode)
                    .maybeSingle();
                const tag = tagResult.data;
                if (!tag?.active || !tag.owner_id) return;
                const profileResult = await themeSupabase
                    .from("profiles")
                    .select("theme_colors")
                    .eq("id",tag.owner_id)
                    .maybeSingle();
                if (profileResult.data?.theme_colors) {
                    applyTheme(profileResult.data.theme_colors);
                }
            } catch (error) {
                console.error("Theme color load error:",error);
            }
        })();
    }

</script>
'''
    men = men.replace("</body>", men_script + "\n</body>", 1)


DASHBOARD.write_text(dashboard, encoding="utf-8")
MEN.write_text(men, encoding="utf-8")
print("Two-color theme system applied.")

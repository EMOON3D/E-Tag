from pathlib import Path


def inject_once(text: str, marker: str, block: str, label: str) -> str:
    if marker not in text:
        raise RuntimeError(f"Marker not found: {label}")
    if block.strip() in text:
        return text
    return text.replace(marker, block + "\n\n" + marker, 1)


def main() -> None:
    dashboard_path = Path("dashboard.html")
    men_path = Path("themes/men.html")

    dashboard = dashboard_path.read_text(encoding="utf-8")
    men = men_path.read_text(encoding="utf-8")

    # ------------------------------------------------------------------
    # DASHBOARD: full visual theme editor
    # ------------------------------------------------------------------
    dashboard_css = r'''
        /* FULL VISUAL THEME COLOR EDITOR */
        .theme-color-editor {
            margin-top: 18px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
        }

        .theme-color-editor h3 {
            margin: 0 0 7px;
            font-size: 17px;
        }

        .theme-color-editor-help {
            margin: 0 0 14px;
            color: #6b7280;
            font-size: 12px;
            line-height: 1.55;
        }

        .theme-color-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 10px;
        }

        .theme-color-item {
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            padding: 11px;
            background: #fafbfc;
        }

        .theme-color-label {
            display: block;
            margin: 0 0 8px;
            font-size: 12px;
            font-weight: 800;
            color: #111827;
        }

        .theme-color-row {
            display: grid;
            grid-template-columns: 44px minmax(0, 1fr);
            gap: 9px;
            align-items: center;
        }

        .theme-color-picker {
            width: 44px;
            height: 40px;
            padding: 3px;
            border: 1px solid #d1d5db;
            border-radius: 10px;
            background: #ffffff;
            cursor: pointer;
        }

        .theme-color-hex {
            width: 100%;
            min-width: 0;
            padding: 9px 10px;
            border: 1px solid #d1d5db;
            border-radius: 9px;
            background: #ffffff;
            color: #111827;
            font: 700 12px Inter, system-ui, sans-serif;
            outline: none;
            text-transform: uppercase;
        }

        .theme-color-hex:focus {
            border-color: #111827;
            box-shadow: 0 0 0 3px rgba(17,24,39,.08);
        }

        .theme-color-actions {
            display: flex;
            justify-content: flex-end;
            gap: 8px;
            margin-top: 12px;
        }

        .theme-color-reset {
            border: 0;
            border-radius: 999px;
            padding: 8px 11px;
            background: #eef2f7;
            color: #374151;
            font-size: 11px;
            font-weight: 800;
            cursor: pointer;
        }

        @media (max-width: 600px) {
            .theme-color-grid {
                grid-template-columns: 1fr;
            }
        }
'''

    dashboard = inject_once(
        dashboard,
        "        .subsection {\n",
        dashboard_css,
        "dashboard theme color CSS",
    )

    dashboard_html = r'''
                <!-- FULL THEME COLOR CUSTOMIZATION -->
                <div
                    id="themeColorEditor"
                    class="theme-color-editor"
                >

                    <h3>
                        Theme Colors
                    </h3>

                    <p class="theme-color-editor-help">
                        Customize the visual palette of your public profile. Text, fonts and social PNG icon colors stay unchanged. The bright/light glass design remains.
                    </p>

                    <div class="theme-color-grid">

                        <div class="theme-color-item">
                            <label class="theme-color-label">Background Start</label>
                            <div class="theme-color-row">
                                <input id="themeBgStartPicker" class="theme-color-picker" type="color" value="#C3CDB8">
                                <input id="themeBgStartHex" class="theme-color-hex" type="text" value="#C3CDB8" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Background Middle</label>
                            <div class="theme-color-row">
                                <input id="themeBgMiddlePicker" class="theme-color-picker" type="color" value="#D3DBC8">
                                <input id="themeBgMiddleHex" class="theme-color-hex" type="text" value="#D3DBC8" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Background End</label>
                            <div class="theme-color-row">
                                <input id="themeBgEndPicker" class="theme-color-picker" type="color" value="#E1E7DA">
                                <input id="themeBgEndHex" class="theme-color-hex" type="text" value="#E1E7DA" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Main Theme</label>
                            <div class="theme-color-row">
                                <input id="themeMainPicker" class="theme-color-picker" type="color" value="#D3DBC8">
                                <input id="themeMainHex" class="theme-color-hex" type="text" value="#D3DBC8" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Secondary Theme</label>
                            <div class="theme-color-row">
                                <input id="themeSecondaryPicker" class="theme-color-picker" type="color" value="#E5EADF">
                                <input id="themeSecondaryHex" class="theme-color-hex" type="text" value="#E5EADF" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Glass Tint</label>
                            <div class="theme-color-row">
                                <input id="themeGlassPicker" class="theme-color-picker" type="color" value="#FFFFFF">
                                <input id="themeGlassHex" class="theme-color-hex" type="text" value="#FFFFFF" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Card Surface</label>
                            <div class="theme-color-row">
                                <input id="themeSurfacePicker" class="theme-color-picker" type="color" value="#FFFFFF">
                                <input id="themeSurfaceHex" class="theme-color-hex" type="text" value="#FFFFFF" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Card Border</label>
                            <div class="theme-color-row">
                                <input id="themeBorderPicker" class="theme-color-picker" type="color" value="#FFFFFF">
                                <input id="themeBorderHex" class="theme-color-hex" type="text" value="#FFFFFF" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Accent</label>
                            <div class="theme-color-row">
                                <input id="themeAccentPicker" class="theme-color-picker" type="color" value="#B8C9A8">
                                <input id="themeAccentHex" class="theme-color-hex" type="text" value="#B8C9A8" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                        <div class="theme-color-item">
                            <label class="theme-color-label">Shadow Tint</label>
                            <div class="theme-color-row">
                                <input id="themeShadowPicker" class="theme-color-picker" type="color" value="#374539">
                                <input id="themeShadowHex" class="theme-color-hex" type="text" value="#374539" maxlength="7" spellcheck="false" autocomplete="off">
                            </div>
                        </div>

                    </div>

                    <div class="theme-color-actions">
                        <button
                            id="resetThemeColors"
                            class="theme-color-reset"
                            type="button"
                        >
                            Reset Theme Colors
                        </button>
                    </div>

                </div>
'''

    # Put it immediately before Personal Information. This keeps it visible
    # without disturbing profile type or avatar controls.
    dashboard = inject_once(
        dashboard,
        "                    <div class=\"subsection\">\n\n                        <h3>\n                            Personal Information\n",
        dashboard_html,
        "dashboard theme color editor HTML",
    )

    # ------------------------------------------------------------------
    # DASHBOARD JS: state, render, save, load, live iframe preview
    # ------------------------------------------------------------------
    state_block = r'''

    const DEFAULT_THEME_COLORS = {
        background_start: "#C3CDB8",
        background_middle: "#D3DBC8",
        background_end: "#E1E7DA",
        main: "#D3DBC8",
        secondary: "#E5EADF",
        glass: "#FFFFFF",
        surface: "#FFFFFF",
        border: "#FFFFFF",
        accent: "#B8C9A8",
        shadow: "#374539"
    };

    let currentThemeColors = {
        ...DEFAULT_THEME_COLORS
    };

    const themeColorBindings = [
        ["background_start", "themeBgStartPicker", "themeBgStartHex"],
        ["background_middle", "themeBgMiddlePicker", "themeBgMiddleHex"],
        ["background_end", "themeBgEndPicker", "themeBgEndHex"],
        ["main", "themeMainPicker", "themeMainHex"],
        ["secondary", "themeSecondaryPicker", "themeSecondaryHex"],
        ["glass", "themeGlassPicker", "themeGlassHex"],
        ["surface", "themeSurfacePicker", "themeSurfaceHex"],
        ["border", "themeBorderPicker", "themeBorderHex"],
        ["accent", "themeAccentPicker", "themeAccentHex"],
        ["shadow", "themeShadowPicker", "themeShadowHex"]
    ];

    function validThemeHex(value) {
        return /^#[0-9A-Fa-f]{6}$/.test(String(value || "").trim());
    }

    function normalizeThemeColor(key, value) {
        const clean = String(value || "").trim().toUpperCase();
        return validThemeHex(clean)
            ? clean
            : DEFAULT_THEME_COLORS[key];
    }

    function renderThemeColorEditor() {
        themeColorBindings.forEach(
            ([key, pickerId, hexId]) => {
                const picker = document.getElementById(pickerId);
                const hex = document.getElementById(hexId);
                const value = normalizeThemeColor(
                    key,
                    currentThemeColors[key]
                );

                currentThemeColors[key] = value;

                if (picker) {
                    picker.value = value;
                }

                if (hex) {
                    hex.value = value;
                }
            }
        );
    }

    function sendThemeColorsToPreview() {
        const frame = document.getElementById("themePreviewFrame");

        if (!frame?.contentWindow) {
            return;
        }

        frame.contentWindow.postMessage(
            {
                type: "etag-theme-colors",
                theme_colors: {
                    ...currentThemeColors
                }
            },
            "*"
        );
    }

    function updateThemeColor(key, value) {
        currentThemeColors[key] = normalizeThemeColor(
            key,
            value
        );

        renderThemeColorEditor();
        sendThemeColorsToPreview();
    }

    function setupThemeColorEditor() {
        themeColorBindings.forEach(
            ([key, pickerId, hexId]) => {
                const picker = document.getElementById(pickerId);
                const hex = document.getElementById(hexId);

                picker?.addEventListener(
                    "input",
                    event => updateThemeColor(key, event.target.value)
                );

                hex?.addEventListener(
                    "change",
                    event => updateThemeColor(key, event.target.value)
                );

                hex?.addEventListener(
                    "blur",
                    () => renderThemeColorEditor()
                );
            }
        );

        document
            .getElementById("resetThemeColors")
            ?.addEventListener(
                "click",
                () => {
                    currentThemeColors = {
                        ...DEFAULT_THEME_COLORS
                    };
                    renderThemeColorEditor();
                    sendThemeColorsToPreview();
                }
            );

        document
            .getElementById("themePreviewFrame")
            ?.addEventListener(
                "load",
                () => sendThemeColorsToPreview()
            );

        renderThemeColorEditor();
    }
'''

    dashboard = inject_once(
        dashboard,
        "    let currentCoverUrl =\n        \"\";",
        state_block,
        "dashboard theme color state",
    )

    # Add theme_colors to the common payload directly after cover_image_url.
    if "            theme_colors:" not in dashboard:
        marker = '''            cover_image_url:
                currentCoverUrl ||
                null,
'''
        replacement = marker + '''
            theme_colors:
                {
                    ...currentThemeColors
                },
'''
        if marker not in dashboard:
            raise RuntimeError("Dashboard profile payload marker not found")
        dashboard = dashboard.replace(marker, replacement, 1)

    # Load saved theme colors next to current cover URL.
    if "...(profile.theme_colors || {})" not in dashboard:
        marker = '''        currentCoverUrl =
            profile.cover_image_url ||
            "";
'''
        replacement = marker + '''
        currentThemeColors = {
            ...DEFAULT_THEME_COLORS,
            ...(profile.theme_colors && typeof profile.theme_colors === "object"
                ? profile.theme_colors
                : {})
        };
'''
        if marker not in dashboard:
            raise RuntimeError("Dashboard profile load marker not found")
        dashboard = dashboard.replace(marker, replacement, 1)

    # Ensure editor is initialized during first render and after loading profile.
    if "setupThemeColorEditor();" not in dashboard:
        marker = "    /*\n     * START DASHBOARD\n     */"
        if marker in dashboard:
            dashboard = dashboard.replace(
                marker,
                "    setupThemeColorEditor();\n\n" + marker,
                1,
            )
        else:
            marker = "    loadDashboard()"
            dashboard = dashboard.replace(
                marker,
                "    setupThemeColorEditor();\n\n" + marker,
                1,
            )

    # Make Save Profile persist the current palette even for existing profiles.
    # The payload injection above is enough; render initializes from saved data.

    # ------------------------------------------------------------------
    # MEN THEME: visual-only palette application.
    # Text and fixed social PNG icons remain untouched.
    # ------------------------------------------------------------------
    men_css = r'''

        /* FULL VISUAL THEME CUSTOMIZATION */
        .theme-customized {
            --tc-bg-start: #C3CDB8;
            --tc-bg-middle: #D3DBC8;
            --tc-bg-end: #E1E7DA;
            --tc-main: #D3DBC8;
            --tc-secondary: #E5EADF;
            --tc-glass: #FFFFFF;
            --tc-surface: #FFFFFF;
            --tc-border: #FFFFFF;
            --tc-accent: #B8C9A8;
            --tc-shadow: #374539;
        }

        .theme-customized body {
            background:
                radial-gradient(
                    ellipse at 70% 18%,
                    rgba(255,255,255,.92) 0%,
                    rgba(255,255,255,.45) 27%,
                    transparent 57%
                ),
                radial-gradient(
                    ellipse at 15% 75%,
                    color-mix(in srgb, var(--tc-secondary) 60%, transparent) 0%,
                    color-mix(in srgb, var(--tc-main) 38%, transparent) 35%,
                    transparent 70%
                ),
                linear-gradient(
                    135deg,
                    var(--tc-bg-start) 0%,
                    var(--tc-bg-middle) 38%,
                    var(--tc-bg-end) 68%,
                    var(--tc-bg-middle) 100%
                );
        }

        .theme-customized .hero::after {
            background: color-mix(in srgb, var(--tc-glass) 38%, transparent);
        }

        .theme-customized .avatar {
            background:
                linear-gradient(
                    145deg,
                    color-mix(in srgb, var(--tc-surface) 88%, white),
                    color-mix(in srgb, var(--tc-main) 58%, white)
                );
            border-color: color-mix(in srgb, var(--tc-border) 74%, transparent);
            box-shadow: 0 12px 30px color-mix(in srgb, var(--tc-shadow) 18%, transparent);
        }

        .theme-customized .contact-item {
            background:
                linear-gradient(
                    100deg,
                    color-mix(in srgb, var(--tc-glass) 58%, transparent),
                    color-mix(in srgb, var(--tc-main) 64%, white)
                );
            border-color: color-mix(in srgb, var(--tc-border) 48%, transparent);
            box-shadow: 0 7px 18px color-mix(in srgb, var(--tc-shadow) 14%, transparent);
        }

        .theme-customized .contact-item:hover {
            background:
                linear-gradient(
                    100deg,
                    color-mix(in srgb, var(--tc-glass) 72%, transparent),
                    color-mix(in srgb, var(--tc-main) 78%, white)
                );
        }

        .theme-customized .contact-icon {
            background: color-mix(in srgb, var(--tc-surface) 54%, transparent);
            border-color: color-mix(in srgb, var(--tc-border) 48%, transparent);
        }

        .theme-customized .social-item {
            background:
                linear-gradient(
                    145deg,
                    color-mix(in srgb, var(--tc-surface) 74%, transparent),
                    color-mix(in srgb, var(--tc-main) 72%, white)
                );
            border-color: color-mix(in srgb, var(--tc-border) 58%, transparent);
            box-shadow: 0 8px 20px color-mix(in srgb, var(--tc-shadow) 17%, transparent);
        }

        .theme-customized .social-item.active {
            background:
                linear-gradient(
                    145deg,
                    color-mix(in srgb, var(--tc-surface) 92%, white),
                    color-mix(in srgb, var(--tc-secondary) 82%, white)
                );
            box-shadow: 0 15px 30px color-mix(in srgb, var(--tc-accent) 22%, transparent);
        }

        .theme-customized .social-line,
        .theme-customized .swipe-line {
            background: color-mix(in srgb, var(--tc-accent) 42%, transparent);
        }

        .theme-customized .bottom {
            background:
                linear-gradient(
                    180deg,
                    transparent,
                    color-mix(in srgb, var(--tc-main) 12%, transparent)
                );
        }
'''

    men = inject_once(
        men,
        "    </style>",
        men_css,
        "Men theme full visual palette CSS",
    )

    men_js = r'''

    const DEFAULT_THEME_COLORS = {
        background_start: "#C3CDB8",
        background_middle: "#D3DBC8",
        background_end: "#E1E7DA",
        main: "#D3DBC8",
        secondary: "#E5EADF",
        glass: "#FFFFFF",
        surface: "#FFFFFF",
        border: "#FFFFFF",
        accent: "#B8C9A8",
        shadow: "#374539"
    };

    function applyThemeColors(colors) {
        const palette = {
            ...DEFAULT_THEME_COLORS,
            ...(colors && typeof colors === "object"
                ? colors
                : {})
        };

        const valid = value =>
            /^#[0-9A-Fa-f]{6}$/.test(String(value || ""));

        Object.keys(DEFAULT_THEME_COLORS).forEach(
            key => {
                const value = valid(palette[key])
                    ? String(palette[key]).toUpperCase()
                    : DEFAULT_THEME_COLORS[key];

                document.documentElement.style.setProperty(
                    `--tc-${key.replace("background_", "bg-")}`,
                    value
                );
            }
        );

        document.documentElement.style.setProperty("--tc-bg-start", palette.background_start);
        document.documentElement.style.setProperty("--tc-bg-middle", palette.background_middle);
        document.documentElement.style.setProperty("--tc-bg-end", palette.background_end);
        document.documentElement.style.setProperty("--tc-main", palette.main);
        document.documentElement.style.setProperty("--tc-secondary", palette.secondary);
        document.documentElement.style.setProperty("--tc-glass", palette.glass);
        document.documentElement.style.setProperty("--tc-surface", palette.surface);
        document.documentElement.style.setProperty("--tc-border", palette.border);
        document.documentElement.style.setProperty("--tc-accent", palette.accent);
        document.documentElement.style.setProperty("--tc-shadow", palette.shadow);
        document.documentElement.classList.add("theme-customized");
    }

    window.addEventListener(
        "message",
        event => {
            if (event.data?.type !== "etag-theme-colors") {
                return;
            }

            applyThemeColors(
                event.data.theme_colors
            );
        }
    );
'''

    # Place the function before load-related functions. This is outside any other function.
    men = inject_once(
        men,
        "    function getTagCode() {",
        men_js,
        "Men theme runtime palette code",
    )

    # Apply saved colors in normal public view immediately after profile fetch.
    if "applyThemeColors(profileData.theme_colors);" not in men:
        marker = '''            const displayName =
                clean(
                    profileData.display_name
                ) ||
                "E-Tag User";'''
        if marker not in men:
            raise RuntimeError("Men public profile display marker not found")
        men = men.replace(
            marker,
            "            applyThemeColors(profileData.theme_colors);\n\n" + marker,
            1,
        )

    # Preview mode uses the profile object received by postMessage. If the existing
    # preview handler is present, a generic message listener above already handles colors.

    dashboard_path.write_text(dashboard, encoding="utf-8")
    men_path.write_text(men, encoding="utf-8")

    print("Full visual theme color customization applied successfully.")


if __name__ == "__main__":
    main()

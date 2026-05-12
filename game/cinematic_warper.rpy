## Registers cinematic_ease as an ATL warper.
## Must be in a separate file parsed before screens.rpy so the warper is
## available when ATL transforms are compiled.
## "cinematic_warper.rpy" sorts before "screens.rpy" alphabetically.

python early:
    import math as _cinematic_math

    @renpy.atl_warper
    def cinematic_ease(t):
        """
        Custom ATL warper driven by cinematic_bars_state["curve"].
        None / "linear"     -> linear (default)
        "ease"              -> slow-fast-slow (smoothstep)
        "easein"            -> starts slow, ends fast
        "easeout"           -> starts fast, ends slow
        "bounce"            -> bounces at the end like a ball dropping
        "elastic"           -> springs past target then snaps back
        [(secs, frac), ...] -> multi-segment curve
        e.g. [(4, 0.2), (1, 0.8)] = slow 4s covering 20%,
        fast 1s covering 80%
        """
        try:
            curve = renpy.store.cinematic_bars_state.get("curve", None)
        except Exception:
            return t
        if not curve or curve == "linear":
            return t
        elif curve == "ease":
            return t * t * (3.0 - 2.0 * t)
        elif curve == "easein":
            return t * t
        elif curve == "easeout":
            return 1.0 - (1.0 - t) ** 2
        elif curve == "bounce":
            # Simulates a ball dropping and bouncing to rest
            u = 1.0 - t
            if u < 1.0 / 2.75:
                return 1.0 - 7.5625 * u * u
            elif u < 2.0 / 2.75:
                u -= 1.5 / 2.75
                return 1.0 - (7.5625 * u * u + 0.75)
            elif u < 2.5 / 2.75:
                u -= 2.25 / 2.75
                return 1.0 - (7.5625 * u * u + 0.9375)
            else:
                u -= 2.625 / 2.75
                return 1.0 - (7.5625 * u * u + 0.984375)
        elif curve == "elastic":
            # Springs past the target then snaps back into place
            if t == 0.0 or t == 1.0:
                return t
            return (2.0 ** (-10.0 * t)) * _cinematic_math.sin((t - 0.075) * (2.0 * _cinematic_math.pi) / 0.3) + 1.0
        elif isinstance(curve, list) and len(curve) > 0:
            total_time = sum(s[0] for s in curve)
            total_dist = sum(s[1] for s in curve)
            if total_time <= 0.0 or total_dist <= 0.0:
                return t
            t_abs = t * total_time
            acc_t = 0.0
            acc_d = 0.0
            for seg_time, seg_dist in curve:
                if t_abs <= acc_t + seg_time + 1e-9:
                    seg_frac = (t_abs - acc_t) / seg_time if seg_time > 0.0 else 1.0
                    return (acc_d + seg_frac * seg_dist) / total_dist
                acc_t += seg_time
                acc_d += seg_dist
            return 1.0
        return t

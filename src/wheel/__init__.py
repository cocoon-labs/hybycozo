
SCHEMES = {
    'red_purple_blue': [(255,0,0), (177,67,226), (0,0,255)],
    'snowskirt': [(218,107,44), (240,23,0), (147,0,131)],
    'royal':     [(0,0,0), (128,0,255), (128,0,128)],
    'cool':      [(122,0,255), (0,0,255), (0,88,205)],
    'dork':      [(0,0,0), (196,0,255), (209,209,209)],
    'sevens':    [(117,0,177), (77,17,71), (247,77,7)],
    'orpal':     [(128,0,255), (0,0,0), (255,128,0)]
}

class ColorWheel(object):
    
    def get_color(self, scheme, position):
        colors = SCHEMES[scheme]
        n_colors = len(colors)
        dist = 255 / n_colors

        for i in xrange(0, n_colors):
            if position < (i+1) * dist:
                return self._gen_color(i, colors, position, dist)

        return self._gen_color(n_colors - 1, colors, position, dist)

    def _gen_color(self, idx, colors, position, dist):
        position = position - (idx * dist)
        n_colors = len(colors)
        return (
            colors[idx][0] + (position * (colors[(idx+1) % n_colors][0] - colors[idx][0]) / dist),
            colors[idx][1] + (position * (colors[(idx+1) % n_colors][1] - colors[idx][1]) / dist),
            colors[idx][2] + (position * (colors[(idx+1) % n_colors][2] - colors[idx][2]) / dist)
        )

                

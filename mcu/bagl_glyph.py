from collections import namedtuple

"""
 {BAGL_GLYPH_ICON_DOWN, 7, 4, 1, C_icon_down_colors, C_icon_down_bitmap},
unsigned int const C_icon_down_colors[] = {
  0x00000000,
  0x00ffffff,

};

unsigned char const C_icon_down_bitmap[] = {
  0x41, 0x11, 0x05, 0x01,
};

typedef struct {
  unsigned int         icon_id;
  unsigned int         width;
  unsigned int         height;
  unsigned int         bits_per_pixel;
  const unsigned int*  default_colors; // color array entry count is (1<<bits_per_pixel)
  const unsigned char* bitmap;
} bagl_glyph_array_entry_t;
"""

Glyph = namedtuple("Glyph", "icon_id width height bpp colors bitmap")

BAGL_GLYPH_ICON_CHECK = 6
BAGL_GLYPH_ICON_CROSS = 7
BAGL_GLYPH_ICON_CHECK_BADGE = 8
BAGL_GLYPH_ICON_LEFT = 9
BAGL_GLYPH_ICON_RIGHT = 10
BAGL_GLYPH_ICON_UP = 11
BAGL_GLYPH_ICON_DOWN = 12
BAGL_GLYPH_ICON_CROSS_BADGE = 14
BAGL_GLYPH_ICON_TRANSACTION_BADGE = 24
BAGL_GLYPH_ICON_EYE_BADGE = 27

GLYPHS = [
    Glyph(
        BAGL_GLYPH_ICON_CHECK,
        8,
        6,
        1,
        [0x00000000, 0x00FFFFFF],
        [0x80, 0x40, 0x20, 0x11, 0x0A, 0x04],
    ),
    Glyph(
        BAGL_GLYPH_ICON_CROSS,
        7,
        7,
        1,
        [0x00000000, 0x00FFFFFF],
        [0x41, 0x11, 0x05, 0x41, 0x11, 0x05, 0x01],
    ),
    Glyph(
        BAGL_GLYPH_ICON_CHECK_BADGE,
        14,
        14,
        1,
        [0x00FFFFFF, 0x00000000],
        [
            0x1F,
            0xFE,
            0x01,
            0x3E,
            0x00,
            0x07,
            0x80,
            0x01,
            0x24,
            0x80,
            0x83,
            0x70,
            0x70,
            0x0E,
            0xF8,
            0x41,
            0x3C,
            0x18,
            0x06,
            0x0E,
            0xC0,
            0x07,
            0xF8,
            0x87,
            0x0F,
        ],
    ),
    Glyph(
        BAGL_GLYPH_ICON_LEFT,
        4,
        7,
        1,
        [0x00000000, 0x00FFFFFF],
        [0x48, 0x12, 0x42, 0x08],
    ),
    Glyph(
        BAGL_GLYPH_ICON_RIGHT,
        4,
        7,
        1,
        [0x00000000, 0x00FFFFFF],
        [0x21, 0x84, 0x24, 0x01],
    ),
    Glyph(
        BAGL_GLYPH_ICON_UP, 7, 4, 1, [0x00000000, 0x00FFFFFF], [0x08, 0x8A, 0x28, 0x08]
    ),
    Glyph(
        BAGL_GLYPH_ICON_DOWN,
        7,
        4,
        1,
        [0x00000000, 0x00FFFFFF],
        [0x41, 0x11, 0x05, 0x01],
    ),
    Glyph(
        BAGL_GLYPH_ICON_CROSS_BADGE,
        14,
        14,
        1,
        [0x00FFFFFF, 0x00000000],
        [
            0x1F,
            0xFE,
            0x01,
            0x3E,
            0x00,
            0x47,
            0x88,
            0x39,
            0x27,
            0xFC,
            0x00,
            0x1E,
            0x80,
            0x07,
            0xF0,
            0x43,
            0xCE,
            0x19,
            0x21,
            0x0E,
            0xC0,
            0x07,
            0xF8,
            0x87,
            0x0F,
        ],
    ),
    Glyph(
        BAGL_GLYPH_ICON_TRANSACTION_BADGE,
        14,
        14,
        1,
        [0x00FFFFFF, 0x00000000],
        [
            0x1F,
            0xFE,
            0x01,
            0x3E,
            0x10,
            0x07,
            0x8C,
            0xF9,
            0x27,
            0xFE,
            0x01,
            0x32,
            0xC0,
            0x04,
            0xF8,
            0x47,
            0xFE,
            0x19,
            0x03,
            0x8E,
            0xC0,
            0x07,
            0xF8,
            0x87,
            0x0F,
        ],
    ),
    Glyph(
        BAGL_GLYPH_ICON_EYE_BADGE,
        14,
        14,
        1,
        [0x00FFFFFF, 0x00000000],
        [
            0x1F,
            0xFE,
            0x01,
            0x3E,
            0x00,
            0x07,
            0x80,
            0xE1,
            0x21,
            0xFE,
            0xC1,
            0xF3,
            0xF0,
            0x3C,
            0xF8,
            0x47,
            0x78,
            0x18,
            0x00,
            0x0E,
            0xC0,
            0x07,
            0xF8,
            0x87,
            0x0F,
        ],
    ),
]


def get(icon_id):
    for glyph in GLYPHS:
        if glyph.icon_id == icon_id:
            return glyph
    return None

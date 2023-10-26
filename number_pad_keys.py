row_1, row_2, row_3, row_4, row_5, row_6 = 10, 60, 125, 190, 255, 320
function_keys_height = 40
all_keys_size = 60

keyboard_keys = [
    # Number pad keys
    {
        "key": ["num_lock"],
        "name": "Num\nLock",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1190,
        "pos_y": row_2
    },
    {
        "key": ["kp_divide"],
        "name": "/",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1255,
        "pos_y": row_2
    },
    {
        "key": ["kp_multiply"],
        "name": "*",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1320,
        "pos_y": row_2
    },
    {
        "key": ["kp_subtract"],
        "name": "-",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1385,
        "pos_y": row_2
    },
    {
        "key": ["kp_add"],
        "name": "+",
        "width": all_keys_size,
        "height": all_keys_size * 2 + 5,
        "pos_x": 1385,
        "pos_y": row_3
    },
    {
        "key": ["kp_enter"],
        "name": "Enter",
        "width": all_keys_size,
        "height": all_keys_size * 2 + 5,
        "pos_x": 1385,
        "pos_y": row_5
    },
    {
        "key": ["kp_decimal", "kp_delete"],
        "name": ".",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1320,
        "pos_y": row_6
    },
    {
        "key": ["kp_0", "kp_insert"],
        "name": "0",
        "width": all_keys_size * 2 + 5,
        "height": all_keys_size,
        "pos_x": 1190,
        "pos_y": row_6
    },
    {
        "key": ["kp_1", "kp_end"],
        "name": "1",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1190,
        "pos_y": row_5
    },
    {
        "key": ["kp_2", "kp_down"],
        "name": "2",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1255,
        "pos_y": row_5
    },
    {
        "key": ["kp_3", "kp_next"],
        "name": "3",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1320,
        "pos_y": row_5
    },
    {
        "key": ["kp_4", "kp_left"],
        "name": "4",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1190,
        "pos_y": row_4
    },
    {
        "key": ["kp_5", "kp_begin"],
        "name": "5",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1255,
        "pos_y": row_4
    },
    {
        "key": ["kp_6", "kp_right"],
        "name": "6",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1320,
        "pos_y": row_4
    },
    {
        "key": ["kp_7", "kp_home"],
        "name": "7",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1190,
        "pos_y": row_3
    },
    {
        "key": ["kp_8", "kp_up"],
        "name": "8",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1255,
        "pos_y": row_3
    },
    {
        "key": ["kp_9", "kp_prior"],
        "name": "9",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1320,
        "pos_y": row_3
    },

    # Arrow keys
    {
        "key": ["left"],
        "name": "⬅️",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 990,
        "pos_y": row_6
    },
    {
        "key": ["down"],
        "name": "⬇️",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1055,
        "pos_y": row_6
    },
    {
        "key": ["right"],
        "name": "➡️",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1120,
        "pos_y": row_6
    },
    {
        "key": ["up"],
        "name": "⬆️️",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1055,
        "pos_y": row_5
    },

    # Addition keys
    {
        "key": ["print"],
        "name": "Print    \nScreen️",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 990,
        "pos_y": row_1
    },
    {
        "key": ["scroll_lock"],
        "name": "Scroll\nLock",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 1055,
        "pos_y": row_1
    },
    {
        "key": ["pause"],
        "name": "Pause\nBreak",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 1120,
        "pos_y": row_1
    },
    {
        "key": ["insert"],
        "name": "Insert",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 990,
        "pos_y": row_2
    },
    {
        "key": ["home"],
        "name": "Home",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1055,
        "pos_y": row_2
    },
    {
        "key": ["prior"],
        "name": "Page\nUp",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1120,
        "pos_y": row_2
    },
    {
        "key": ["delete"],
        "name": "️Delete",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 990,
        "pos_y": row_3
    },
    {
        "key": ["end"],
        "name": "End",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1055,
        "pos_y": row_3
    },
    {
        "key": ["next"],
        "name": "Page\nDown",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 1120,
        "pos_y": row_3
    },

    # Function keys
    {
        "key": ["f1"],
        "name": "F1",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 140,
        "pos_y": row_1
    },
    {
        "key": ["f2"],
        "name": "F2",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 205,
        "pos_y": row_1
    },
    {
        "key": ["f3"],
        "name": "F3",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 270,
        "pos_y": row_1
    },
    {
        "key": ["f4"],
        "name": "F4",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 335,
        "pos_y": row_1
    },
    {
        "key": ["f5"],
        "name": "F5",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 435,
        "pos_y": row_1
    },
    {
        "key": ["f6"],
        "name": "F6",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 500,
        "pos_y": row_1
    },
    {
        "key": ["f7"],
        "name": "F7",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 565,
        "pos_y": row_1
    },
    {
        "key": ["f8"],
        "name": "F8",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 630,
        "pos_y": row_1
    },
    {
        "key": ["f9"],
        "name": "F9",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 725,
        "pos_y": row_1
    },
    {
        "key": ["f10"],
        "name": "F10",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 790,
        "pos_y": row_1
    },
    {
        "key": ["f11"],
        "name": "F11",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 855,
        "pos_y": row_1
    },
    {
        "key": ["f12"],
        "name": "F12",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 920,
        "pos_y": row_1
    },

    # Number keys
    {
        "key": ["1", "exclam"],
        "name": "!      \n  1",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 75,
        "pos_y": row_2
    },
    {
        "key": ["2", "at"],
        "name": "@      \n  2",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 140,
        "pos_y": row_2
    },
    {
        "key": ["3", "numbersign"],
        "name": "#      \n  3",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 205,
        "pos_y": row_2
    },
    {
        "key": ["4", "dollar"],
        "name": "%      \n  4",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 270,
        "pos_y": row_2
    },
    {
        "key": ["5", "percent"],
        "name": "%      \n  5",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 335,
        "pos_y": row_2
    },
    {
        "key": ["6", "asciicircum"],
        "name": "^      \n  6",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 400,
        "pos_y": row_2
    },
    {
        "key": ["7", "ampersand"],
        "name": "&      \n  7",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 465,
        "pos_y": row_2
    },
    {
        "key": ["8", "asterisk"],
        "name": "*      \n  8",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 530,
        "pos_y": row_2
    },
    {
        "key": ["9", "parenleft"],
        "name": "(      \n  9",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 595,
        "pos_y": row_2
    },
    {
        "key": ["0", "parenright"],
        "name": ")      \n  0",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 660,
        "pos_y": row_2
    },
    {
        "key": ["underscore", "minus"],
        "name": "_      \n  -",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 725,
        "pos_y": row_2
    },
    {
        "key": ["plus", "equal"],
        "name": "+      \n  =",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 790,
        "pos_y": row_2
    },

    # Manage keys
    {
        "key": ["escape"],
        "name": "Esc",
        "width": all_keys_size,
        "height": function_keys_height,
        "pos_x": 10,
        "pos_y": row_1
    },
    {
        "key": ["grave", "asciitilde"],
        "name": "~      \n  `",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 10,
        "pos_y": row_2
    },
    {
        "key": ["tab", "iso_left_tab"],
        "name": "Tab",
        "width": all_keys_size + 35,
        "height": all_keys_size,
        "pos_x": 10,
        "pos_y": row_3
    },
    {
        "key": ["caps_lock"],
        "name": "Caps Lock",
        "width": all_keys_size + 50,
        "height": all_keys_size,
        "pos_x": 10,
        "pos_y": row_4
    },
    {
        "key": ["shift_l"],
        "name": "Shift",
        "width": all_keys_size + 85,
        "height": all_keys_size,
        "pos_x": 10,
        "pos_y": row_5
    },
    {
        "key": ["control_l"],
        "name": "Ctrl",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 10,
        "pos_y": row_6
    },
    {
        "key": ["win", "super"],
        "name": "Win",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 100,
        "pos_y": row_6
    },
    {
        "key": ["space", "iso_next_group"],
        "name": "Space",
        "width": all_keys_size + 280,
        "height": all_keys_size,
        "pos_x": 280,
        "pos_y": row_6
    },
    {
        "key": ["alt_l"],
        "name": "Alt",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 190,
        "pos_y": row_6
    },
    {
        "key": ["alt_r"],
        "name": "Alt",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 625,
        "pos_y": row_6
    },
    {
        "key": ["fn"],
        "name": "Fn",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 715,
        "pos_y": row_6
    },
    {
        "key": ["control_r"],
        "name": "Ctrl",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 895,
        "pos_y": row_6
    },
    {
        "key": ["menu"],
        "name": "Menu",
        "width": all_keys_size + 25,
        "height": all_keys_size,
        "pos_x": 805,
        "pos_y": row_6
    },
    {
        "key": ["shift_r"],
        "name": "Shift",
        "width": 170,
        "height": all_keys_size,
        "pos_x": 810,
        "pos_y": row_5
    },
    {
        "key": ["return"],
        "name": "Enter",
        "width": 140,
        "height": all_keys_size,
        "pos_x": 840,
        "pos_y": row_4
    },
    {
        "key": ["backslash", "bar"],
        "name": "|      \n  \\",
        "width": all_keys_size + 30,
        "height": all_keys_size,
        "pos_x": 890,
        "pos_y": row_3
    },
    {
        "key": ["backspace"],
        "name": "BackSpace",
        "width": all_keys_size + 65,
        "height": all_keys_size,
        "pos_x": 855,
        "pos_y": row_2
    },
    {
        "key": ["bracketleft", "braceleft"],
        "name": "{      \n  [",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 760,
        "pos_y": row_3
    },
    {
        "key": ["bracketright", "braceright"],
        "name": "}      \n  ]",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 825,
        "pos_y": row_3
    },
    {
        "key": ["semicolon", "colon"],
        "name": ":      \n  ;",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 710,
        "pos_y": row_4
    },
    {
        "key": ["quotedbl", "apostrophe"],
        "name": "\"      \n  '",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 775,
        "pos_y": row_4
    },
    {
        "key": ["comma", "less"],
        "name": "<      \n  ,",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 615,
        "pos_y": row_5
    },
    {
        "key": ["period", "greater"],
        "name": ">      \n  .",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 680,
        "pos_y": row_5
    },
    {
        "key": ["slash", "question"],
        "name": "?      \n  /",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 745,
        "pos_y": row_5
    },

    # Letter keys
    {
        "key": ["q", "Q"],
        "name": "Q",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 110,
        "pos_y": row_3
    },
    {
        "key": ["w", "W"],
        "name": "W",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 175,
        "pos_y": row_3
    },
    {
        "key": ["e", "E"],
        "name": "E",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 240,
        "pos_y": row_3
    },
    {
        "key": ["r", "R"],
        "name": "R",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 305,
        "pos_y": row_3
    },
    {
        "key": ["t", "T"],
        "name": "T",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 370,
        "pos_y": row_3
    },
    {
        "key": ["y", "Y"],
        "name": "Y",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 435,
        "pos_y": row_3
    },
    {
        "key": ["u", "U"],
        "name": "U",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 500,
        "pos_y": row_3
    },
    {
        "key": ["i", "I"],
        "name": "I",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 565,
        "pos_y": row_3
    },
    {
        "key": ["o", "O"],
        "name": "O",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 630,
        "pos_y": row_3
    },
    {
        "key": ["p", "P"],
        "name": "P",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 695,
        "pos_y": row_3
    },
    {
        "key": ["a", "A"],
        "name": "A",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 125,
        "pos_y": row_4
    },
    {
        "key": ["s", "S"],
        "name": "S",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 190,
        "pos_y": row_4
    },
    {
        "key": ["d", "D"],
        "name": "D",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 255,
        "pos_y": row_4
    },
    {
        "key": ["f", "F"],
        "name": "F",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 320,
        "pos_y": row_4
    },
    {
        "key": ["g", "G"],
        "name": "G",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 385,
        "pos_y": row_4
    },
    {
        "key": ["h", "H"],
        "name": "H",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 450,
        "pos_y": row_4
    },
    {
        "key": ["j", "J"],
        "name": "J",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 515,
        "pos_y": row_4
    },
    {
        "key": ["k", "K"],
        "name": "K",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 580,
        "pos_y": row_4
    },
    {
        "key": ["l", "L"],
        "name": "L",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 645,
        "pos_y": row_4
    },
    {
        "key": ["z", "Z"],
        "name": "Z",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 160,
        "pos_y": row_5
    },
    {
        "key": ["x", "X"],
        "name": "X",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 225,
        "pos_y": row_5
    },
    {
        "key": ["c", "C"],
        "name": "C",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 290,
        "pos_y": row_5
    },
    {
        "key": ["v", "V"],
        "name": "V",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 355,
        "pos_y": row_5
    },
    {
        "key": ["b", "B"],
        "name": "B",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 420,
        "pos_y": row_5
    },
    {
        "key": ["n", "N"],
        "name": "N",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 485,
        "pos_y": row_5
    },
    {
        "key": ["m", "M"],
        "name": "M",
        "width": all_keys_size,
        "height": all_keys_size,
        "pos_x": 550,
        "pos_y": row_5
    },
]
# -*- coding: utf-8 -*-

class mino_shapes():
    mino_shapes = [
            # MINO_TYPE_I
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 1, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [0, 0, 0, 0],
		            [1, 1, 1, 1],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 1, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 0, 0],
		            [1, 1, 1, 1],
		            [0, 0, 0, 0],
		            [0, 0, 0, 0]
		        ],
		    ],
		    # MINO_TYPE_O
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		    ],
		    # MINO_TYPE_S
		    [
		        # MINO_ANGLE_0
		        [
                    [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [1, 1, 0, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 1, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [1, 1, 0, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 1, 0]
		        ],
		    ],
		    # MINO_TYPE_Z
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 0, 0, 0],
		            [1, 1, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [0, 0, 1, 0],
		            [0, 1, 1, 0],
		            [0, 1, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 1, 1],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 1, 0],
		            [0, 1, 1, 0],
		            [0, 1, 0, 0],
		            [0, 0, 0, 0]
		        ],
		    ],
		    # MINO_TYPE_J
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 0, 1, 0],
		            [0, 0, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [1, 1, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 0, 0],
		            [0, 1, 0, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 1, 1],
		            [0, 0, 0, 0]
		        ],
		    ],
		    # MINO_TYPE_L
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 1, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [0, 0, 1, 0],
		            [1, 1, 1, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 1, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 0, 0],
		            [0, 1, 1, 1],
		            [0, 1, 0, 0],
		            [0, 0, 0, 0]
		        ],
		    ],
		    # MINO_TYPE_T
		    [
		        # MINO_ANGLE_0
		        [
		            [0, 0, 0, 0],
		            [1, 1, 1, 0],
		            [0, 1, 0, 0],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_90
		        [
		            [0, 0, 0, 0],
		            [0, 1, 0, 0],
		            [0, 1, 1, 0],
		            [0, 1, 0, 0]
		        ],
		        # MINO_ANGLE_180
		        [
		            [0, 0, 0, 0],
		            [0, 0, 1, 0],
		            [0, 1, 1, 1],
		            [0, 0, 0, 0]
		        ],
		        # MINO_ANGLE_270
		        [
		            [0, 0, 1, 0],
		            [0, 1, 1, 0],
		            [0, 0, 1, 0],
		            [0, 0, 0, 0]
		        ],
		    ]
		]
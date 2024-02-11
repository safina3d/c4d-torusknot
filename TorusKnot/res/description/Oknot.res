CONTAINER Oknot {
    INCLUDE Obase;
    NAME Oknot;

    GROUP ID_OBJECTPROPERTIES {

        LONG KNOT_PREDEFINED_KNOT_LIST
        {
            CYCLE
            {
                KNOT_PREDEFINED_KNOT_0;
                KNOT_PREDEFINED_KNOT_1;
                KNOT_PREDEFINED_KNOT_2;
                KNOT_PREDEFINED_KNOT_3;
                KNOT_PREDEFINED_KNOT_4;
                KNOT_PREDEFINED_KNOT_5;
                KNOT_PREDEFINED_KNOT_6;
                KNOT_PREDEFINED_KNOT_7;
                KNOT_PREDEFINED_KNOT_8;
                KNOT_PREDEFINED_KNOT_9;
                KNOT_PREDEFINED_KNOT_10;
                KNOT_PREDEFINED_KNOT_11;
                KNOT_PREDEFINED_KNOT_12;
                KNOT_PREDEFINED_KNOT_13;
                KNOT_PREDEFINED_KNOT_14;
                KNOT_PREDEFINED_KNOT_15;
                KNOT_PREDEFINED_KNOT_16;
                KNOT_PREDEFINED_KNOT_17;
                KNOT_PREDEFINED_KNOT_18;
                KNOT_PREDEFINED_KNOT_19;
                KNOT_PREDEFINED_KNOT_20;
                KNOT_PREDEFINED_KNOT_21;
                KNOT_PREDEFINED_KNOT_22;
                KNOT_PREDEFINED_KNOT_23;
                KNOT_PREDEFINED_KNOT_24;
                KNOT_PREDEFINED_KNOT_25;
                KNOT_PREDEFINED_KNOT_26;
                KNOT_PREDEFINED_KNOT_27;
                KNOT_PREDEFINED_KNOT_28;
                KNOT_PREDEFINED_KNOT_29;
                KNOT_PREDEFINED_KNOT_30;
                KNOT_PREDEFINED_KNOT_31;
                KNOT_PREDEFINED_KNOT_32;
                KNOT_PREDEFINED_KNOT_33;
                KNOT_PREDEFINED_KNOT_34;
                KNOT_PREDEFINED_KNOT_35;
                KNOT_PREDEFINED_KNOT_36;
            }
        }

        SEPARATOR { LINE; }

        REAL KNOT_RANGE_MIN { STEP 0.01; }
        REAL KNOT_RANGE_MAX { STEP 0.01; }
        REAL KNOT_STEP { MIN 0.001; STEP 0.001; }

        SEPARATOR { }

        REAL KNOT_PARAM_R0  { STEP 0.01; }
        REAL KNOT_PARAM_R1  { STEP 0.01; }
        REAL KNOT_PARAM_P   { STEP 0.01; }
        REAL KNOT_PARAM_Q   { STEP 0.01; }

        SEPARATOR { }

        BOOL KNOT_CUBIC_INTERPOLATION { }
        BOOL KNOT_CLOSE_SPLINE  { }

        SEPARATOR { }

        STATICTEXT KNOT_POINT_COUNT { }
    }
}


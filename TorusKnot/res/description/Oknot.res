CONTAINER Oknot {
    INCLUDE Obase;
    NAME Oknot;

    GROUP ID_OBJECTPROPERTIES {

        REAL KNOT_RANGE_MIN { STEP 0.01; }
        REAL KNOT_RANGE_MAX { STEP 0.01; }
        REAL KNOT_STEP { MIN 0.001; STEP 0.001; }

        SEPARATOR { }

        REAL KNOT_PARAM_R0  { STEP 0.01; }
        REAL KNOT_PARAM_R1  { STEP 0.01; }
        REAL KNOT_PARAM_N   { STEP 0.01; }

        SEPARATOR { }

        BOOL KNOT_CUBIC_INTERPOLATION { }
        BOOL KNOT_CLOSE_SPLINE  { }

        SEPARATOR { }

        STATICTEXT KNOT_POINT_COUNT { }
        
    }
}
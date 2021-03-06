function sentinel-swap-middle-button () {
    # Storm Sentinel mouse: swap middle-button(2) and thumb1 (8)
    VERBOSE='false'
    UNDO='false'
    for opt in "$@"; do
	case $opt in
	  -v|--verbose )    VERBOSE='true'    ;;
	  -d|--duplicate )  DUPLICATE='true'  ;;
	  -u|--undo )       UNDO='true'       ;;
	esac
    done
    MOUSE_ID=`xinput list | grep -i STORM\ SENTINEL | tail -n1 | cut -f2`
    MOUSE_ID=${MOUSE_ID#id=}
    if [ $VERBOSE == 'true' ]; then echo -ne "Storm Sentinel Mouse ID:\t$MOUSE_ID\n"; fi
    if [ ! -z $MOUSE_ID ]; then
	if   [ $DUPLICATE == 'true' ]; then xinput set-button-map $MOUSE_ID 1 2 3 4 5 6 7 2 9;
	elif [ $UNDO == 'true' ];      then xinput set-button-map $MOUSE_ID 1 2 3 4 5 6 7 8 9;
	else                                xinput set-button-map $MOUSE_ID 1 8 3 4 5 6 7 2 9;
	fi
    fi
    if [ $VERBOSE == 'true' ]; then
	echo -ne "Storm Sentinel Button Map:\t"
	xinput get-button-map ${MOUSE_ID#id=}
    fi
}

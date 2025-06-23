#!/usr/bin/env bash

FILE='.latexminted_config'

if [[ ! ( -f "$HOME/$FILE" || -f "$TEXMF/$FILE" ) ]]; then
    echo 'Error:'
    echo "  Neither $HOME/$FILE (~/$FILE) nor $TEXMF/$FILE (\$TEXMF/$FILE) seem to exist!"
    echo 
    echo '  To create the file, please run: '
    echo '    ./tools/create_latexminted_config.sh'  
    echo ''
    echo '  Or, manually create the file, with at least the following options set:'
    echo
    echo '  {'
    echo '    "security": {' 
    echo '      "enable_cwd_config": true' 
    echo '    }' 
    echo '  }' 
    exit 1
fi

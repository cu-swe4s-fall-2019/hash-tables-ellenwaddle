test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

test ! -f ascii_hash_function.png #is a figure made?

python hash_functions.py random.txt ascii | python scatter.py ascii_hash_function.png "hw" "hv" "title"

test f ascii_hash_function.png


test -f rolling_hash_function.png

python hash_functions.py random.txt rolling | python scatter.py rolling_hash_function.png "hw" "hv" "title"

test f rolling_hash_function.png


test f square_hash_function.png

python hash_functions.py random.txt square | python scatter.py square_hash_function.png "hw" "hv" "title"

test -f square_hash_function.png

rm square_hash_function.png
rm rolling_hash_function.png
rm ascii_hash_function.png

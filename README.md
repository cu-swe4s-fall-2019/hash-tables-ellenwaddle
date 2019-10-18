# Hash tables
python hash_tables.py 1000  ascii linear random.txt 1000 | python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

python hash_functions.py random.txt ascii | python scatter.py ascii_hash_function.png 'hashed random word' 'hashed ascii value'

python hash_tables.py random.txt ascii chain | python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

python hash_tables.py rand_ints.txt rolling linear| python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

python hash_tables.py rand_ints.txt rolling chain| python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

python hash_tables.py rand_ints.txt square linear | python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

python hash_tables.py rand_ints.txt square chain | python scatter.py ascii_hash_function.png "Hashed word" "Hashed value"

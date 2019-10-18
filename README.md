# Hash tables

python hash_functions.py random.txt ascii | python scatter.py ascii_hash_function.png 'hashed random word' 'hashed ascii value'
! [ascii hash function] https://github.com/cu-swe4s-fall-2019/hash-tables-ellenwaddle/ascii_hash_function.png

python hash_functions.py random.txt rolling | python scatter.py rolling_hash_function.png "Hashed word" "Hashed value"
! [rolling hash function] https://github.com/cu-swe4s-fall-2019/hash-tables-ellenwaddle/rolling_hash_function.png

python hash_functions.py rand_ints.txt rolling | python scatter.py rolling_hash_function_ints.png "Hashed word" "Hashed value"
! [rolling hash function with integers] https://github.com/cu-swe4s-fall-2019/hash-tables-ellenwaddle/rolling_hash_function_ints.png

python hash_functions.py random.txt square | python scatter.py square_hash_function_ints.png "Hashed word" "Hashed value"
! [square hash function with integers] https://github.com/cu-swe4s-fall-2019/hash-tables-ellenwaddle/square_hash_function_ints.png


For hash table construction, few things to consider:
1. hash_funcitons is a module that can either take a key and length and returns hash based on ASCII characters, or based on polynomial hash algorithm, or a square algorithm.
2. two types of probes for searching and inserting/finding hash lcoations exist in module called hash_tables.py. Depending on the size you specify for your table, linear probe will probably be slower if you're working with lots of data.
3. can use files random.txt which has random words (for ASCII testing) or rand_ints.txt for playing around with hash funcitons (or use your own data file).  

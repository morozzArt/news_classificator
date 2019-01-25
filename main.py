import train
import test
import time


start_time = time.time()
tuple_from_learning = train.learning()
test.testing(tuple_from_learning)
print("--- %s seconds ---" % (time.time() - start_time))
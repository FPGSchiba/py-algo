import numpy as np
from matplotlib import pyplot as plt

from sorting.comparision import insertion_sort

from utils import Stopwatch

NUM_EXAMPLES = 800

RANDOM_ARRAY = np.random.randint(NUM_EXAMPLES, size=NUM_EXAMPLES)

stopwatch = Stopwatch()
stopwatch.start()
sorted_array = insertion_sort(list(RANDOM_ARRAY))  # Change Algorithm
stopwatch.stop()

if NUM_EXAMPLES <= 3000:
    plt.rcdefaults()
    fig, axs = plt.subplots(2)

    axs[0].barh(np.arange(NUM_EXAMPLES), RANDOM_ARRAY, align='center')
    axs[0].set_title('Example Array')

    axs[1].barh(np.arange(NUM_EXAMPLES), sorted_array, align='center')
    axs[1].set_title('Sorted Array')
    axs[1].text(0.5, 0.1, f'Time used: {stopwatch.get_time_string()}', horizontalalignment='center',
                verticalalignment='center',
                transform=axs[1].transAxes)
    plt.show()
else:
    print("=" * 12 + " EVALUATION " + "=" * 12)
    print("=" * 2 + f" Calculated Array-Size: {NUM_EXAMPLES} " + "=" * 2)
    print("=" * 2 + f" Time: {stopwatch.get_time_string()} " + "=" * 2)

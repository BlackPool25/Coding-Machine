#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdint> // For int64_t

using namespace std;

const int64_t SEGMENT_SIZE = 1 << 20; // ~1 million per segment
const int64_t TARGET_PRIME_INDEX = 100000000;

vector<int> simple_sieve(int64_t limit) {
    vector<bool> is_prime(limit + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int64_t i = 2; i * i <= limit; ++i) {
        if (is_prime[i]) {
            for (int64_t j = i * i; j <= limit; j += i) {
                is_prime[j] = false;
            }
        }
    }

    vector<int> primes;
    for (int64_t i = 2; i <= limit; ++i) {
        if (is_prime[i]) primes.push_back(i);
    }

    return primes;
}

int main() {
    int64_t n = TARGET_PRIME_INDEX;
    double estimate = n * (log(n) + log(log(n)));
    int64_t limit = static_cast<int64_t>(estimate + 10);
    int64_t sqrt_limit = static_cast<int64_t>(sqrt(limit)) + 1;

    vector<int> base_primes = simple_sieve(sqrt_limit);

    int64_t count = 0;
    int64_t low = 2;
    int64_t high = low + SEGMENT_SIZE;

    while (low <= limit) {
        if (high > limit) high = limit + 1;
        vector<bool> is_prime(high - low, true);

        for (int prime : base_primes) {
            int64_t start = max(prime * prime, ((low + prime - 1) / prime) * prime);
            for (int64_t j = start; j < high; j += prime) {
                is_prime[j - low] = false;
            }
        }

        for (int64_t i = low; i < high; ++i) {
            if (is_prime[i - low]) {
                ++count;
                if (count == n) {
                    cout << "The " << TARGET_PRIME_INDEX << "th prime number is: " << i << endl;
                    return 0;
                }
            }
        }

        low = high;
        high += SEGMENT_SIZE;
    }

    cout << "Prime not found in estimated range." << endl;
    return 1;
}

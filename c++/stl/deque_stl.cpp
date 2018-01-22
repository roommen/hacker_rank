#include <iostream>

int main(int argc, char **argv) {
    int T;
    std::cin >> T;
    while (T) {
        int N; std::cin >> N;
        int K; std::cin >> K;

        int A[N];
        for (int i = 0; i < N; ++i) {
            std::cin >> A[i];
        }

        int max = 0;
        for (int i = 0; i <= (N-K); ++i)
        {
            max = A[i];
            for (int j = 1; j < K; ++j) {
                if (A[i+j] > max) {
                    max = A[i+j];
                }
            }
            std::cout << max << " ";
        }
        std::cout << std::endl;
        --T;
    }
    return 0;
}

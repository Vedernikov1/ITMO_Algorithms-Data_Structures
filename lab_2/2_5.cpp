#include <iostream>
#include <vector>


using namespace std;


int QS(vector<int> &array, int low, int high, int k) {

    int low1 = low;
    int high1 = high;
    int elem = array[(low1 + high1) / 2];

    while (low1 <= high1) {

        while (array[low1] < elem) {
            low1++;
        }
        while (array[high1] > elem) {
            high1--;
        }
        if (low1 <= high1) {
            swap(array[low1++], array[high1--]);
        }
    }
    if (k >= low1) {
        QS(array, low1, high, k);
    }
    if (k <= high1) {
        QS(array, low, high1, k);
    }

    return array[k];
}

int main() {

    int n, k, A, B, C;
    cin >> n >> k;
    cin >> A >> B >> C;
    vector<int> arr(n);
    int t0, t1;
    cin >> t0 >> t1;
    arr[0] = t0;
    arr[1] = t1;
    for(int i=2; i<n; i++) {
        arr[i] = A*arr[i-2] + B*arr[i-1] + C;
    }
    cout << QS(arr, 0, n-1, k-1);
}

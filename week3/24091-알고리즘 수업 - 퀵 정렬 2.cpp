#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int n, k;
vector<int> li;
int cnt = 0;

void quick_sort(vector<int>& A, int p, int r);
int partition(vector<int>& A, int p, int r);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;
    li.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> li[i];
    }

    quick_sort(li, 0, li.size() - 1);

    cout << -1 << "\n";
    return 0;
}

void quick_sort(vector<int>& A, int p, int r) {
    if (p < r) {
        int q = partition(A, p, r);
        quick_sort(A, p, q - 1);
        quick_sort(A, q + 1, r);
    }
}

int partition(vector<int>& A, int p, int r) {
    int x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++) {
        if (A[j] <= x) {
            i++;
            swap(A[i], A[j]);
            cnt++;
            if (cnt == k) {
                for (int num : A) {
                    cout << num << " ";
                }
                cout << "\n";
                exit(0);
            }
        }
    }
    if (i + 1 != r) {
        swap(A[i + 1], A[r]);
        cnt++;
        if (cnt == k) {
            for (int num : A) {
                cout << num << " ";
            }
            cout << "\n";
            exit(0);
        }
    }
    return i + 1;
}

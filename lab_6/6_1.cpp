#include <iostream>
#include "fstream"
#include "vector"

using namespace std;

long long hf(int key) {
    long long val = (key * 29831 + 2321800000) % 214787757;
    if (val) return val;
    else return -val;
}

void insert(vector<int> *arr, int key, int num) {
    long long pos = hf(key) % num;
    unsigned int len = arr[pos].size();
    for (int i = 0; i < len; ++i) if (arr[pos][i] == key) return;
    arr[pos].push_back(key);
}

void extract(vector<int> *arr, int key, int num) {
    long long pos = hf(key) % num;
    unsigned int len = arr[pos].size();
    for (int i = 0; i < len; ++i) {
        if (arr[pos][i] == key) {
            arr[pos].erase(arr[pos].begin() + i);
            return;
        }
    }
}

string exists(vector<int> *arr, int key, int num) {
    long long pos = hf(key) % num;
    unsigned int len = arr[pos].size();
    for (int i = 0; i < len; ++i) {
        if (arr[pos][i] == key) return "true\n";
    }
    return "false\n";
}


int main() {
    int num = 100000, key;
    vector<int> arr[100001];

    ifstream f_in("set.in");
    ofstream f_out("set.out");

    string command;
    while (f_in >> command) {
        f_in >> key;
        if (command[0] == 'i') insert(arr, key, num);
        else if (command[0] == 'd') extract(arr, key, num);
        else if (command[0] == 'e') f_out << exists(arr, key, num);
    }
    return 0;
}

#include <vector>
#include <fstream>
#include <sstream>

using std::vector;
using std::ifstream;
using std::istringstream;
using std::string;

typedef vector<vector<string> > Rows;

int main(int argc, char** argv) {
    
    if(argc != 2) return -1;

    ifstream input(argv[1]);

    Rows rows;

    char const row_delim = '\n';
    char const field_delim = '\t';

    for (string row; getline(input, row, row_delim); ) {
      rows.push_back(Rows::value_type());
      istringstream ss(row);
      for (string field; getline(ss, field, field_delim); ) {
        rows.back().push_back(field);
      }
    }
}
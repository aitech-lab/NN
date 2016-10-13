#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <regex>
#include <locale>

using std::wcout;
using std::vector;
using std::wifstream;
using std::wistringstream;
using std::wstring;
using std::regex;
using std::regex_replace;
using std::locale;

typedef vector<vector<wstring> > Rows;

int main(int argc, char** argv) {
    
    if(argc != 2) return -1;

    wifstream input(argv[1]);

    Rows rows;

    wchar_t const row_delim = L'\n';
    wchar_t const field_delim = L'\t';

    for (wstring row; getline(input, row, row_delim); ) {
        rows.push_back(Rows::value_type());
        wistringstream ss(row);
        for (wstring field; getline(ss, field, field_delim); ) {
          rows.back().push_back(field);
        }
    }
    
    // locale old;
    // locale::global(locale("ru_RU.UTF-8"));

    wcout << "PARSED\n" << rows.size() << "\n";

    regex re(R"(\|.*?\}|&.*;|\\s|[\{\}.,!?:/\(\)\[\]]+|\s-|-\s)");
    for(int i = 0; i< rows.size(); i++) {
        vector<wstring> &row = rows[i];
        
        wcout << i<< "\n";

        if(row.size()==2) {
            wcout << row[0] << "\n";
            // wstring cleaned = wregex_replace(row[0], re, "");
            // wcout << cleaned << "\t" << row[1] << "\n";
        } 
    }    

    // locale::global(old);

}
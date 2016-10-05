

#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <unordered_map>

#include <dirent.h>
#include <zip.h>

using std::string;
using std::strtok;
using std::stoi;
using std::vector;
using std::unordered_map;
using std::cout;
using std::cerr;
using std::endl;

static unordered_map<string, int> load_data(string path);
static void load_zip(unordered_map<string, int> &results, const string path);

int main() {
    unordered_map<string, int> data = load_data("./data");
    cerr << "Loaded " << data.size() << " unic lines" << endl;
    for( const auto& n : data ) {
        cout << n.first << "\t" << n.second << endl;
    }
}

static unordered_map<string, int>
load_data(string path) {
    
    unordered_map<string, int> data;
    struct dirent *entry;
    
    DIR *dp;
    dp = opendir("./data");
    if (dp == NULL) {
      return data;
    }

    while((entry = readdir(dp))) {
        string name = entry->d_name;
        string ext = name.substr(name.find_last_of(".")+1);
        if(entry->d_type == DT_REG && ext == "zip")
            load_zip(data, path+"/"+name);
    }
    closedir(dp);

    return data;
}

static void
load_zip(
    unordered_map<string, int> &results, 
    const string path) {

    cerr << "LOAD "<< path << endl;

    int err = 0;
    zip *z = zip_open(path.c_str(), 0, &err);
    for(int i = 0; i < zip_get_num_entries(z, 0); i++) {
        struct zip_stat st;
        if (zip_stat_index(z, i, 0, &st) == 0) {
            cerr << "\t" << st.name << "\t" << st.size << endl;
            char contents[st.size];
            zip_file *f = zip_fopen_index(z, i, 0);
            zip_fread(f, contents, st.size);
            zip_fclose(f);
            
            char *t = strtok(contents, "\n");
            t = strtok(NULL, "\n"); // header
            while (t) {
                string text = "";
                int score = 0;
                t = strtok(NULL, "\t"); // url
                t = strtok(NULL, "\t"); // text
                if(t) text = t;
                t = strtok(NULL, "\t"); // score
                if(t) score = stoi(t);
                t = strtok(NULL, "\n"); // next line
                if(text != "" && score != 0 && results[text]<score) results[text] = score;
            }
        }
    }
    zip_close(z);
}

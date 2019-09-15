#include <iostream>
#include<fstream>
#include<iomanip>
#include<string>


using namespace std;
void permute(string s);
void combin(string s, int len);

int main()
{
    string pstring;
    cout << endl;
    cout<<"Enter a string to find all its permutation "<<endl;
    cin>>pstring;
    cout << "permute: " << endl;
    permute(pstring);
}
/*
void indent(int n){
    int i;
    for(i=0; i< n; i++)
    {
        cout << "   "  ;
    }

}
*/
void permuteHelper(string s , string chosen){
    //indent(chosen.length());
    //cout << "permuteHelper(\"" << s << "\",\"" << chosen << "\")"<< endl;
    //if/else
    if(s.empty())
        cout << chosen << endl;
    else{
        int i;
        //choose /explore/unchoose
        //(1 letter)
        for(i=0; i<s.length(); i++){
            //choose
            char c = s[i] ;
            chosen += c;
            s.erase(i, 1);

            // explore
            permuteHelper(s, chosen);

            //un-choose
            s.insert(i, 1, c);
            chosen.erase(chosen.length()-1, 1);


        }
    }

}
// Print all the possible rearrangements of the characters of the given string
void permute(string s){
    permuteHelper(s, "");
}


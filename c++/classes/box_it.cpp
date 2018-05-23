#include<bits/stdc++.h>

using namespace std;

class Box {
private:
    int l, b, h;
public:
    Box(): l(0), b(0), h(0) {}
    Box(int length, int breadth, int height): l(length), b(breadth), h(height) {}
    Box(const Box& b) {
        l = b.l;
        b = b.b;
        h = b.h;
    }
    int getLength() { return l; }
    int getBreadth() { return b; }
    int getHeight() { return h; }
    long long CalculateVolume() { return l*b*h; }
    bool operator <(Box b) {
        if(l < b.l) {
            if((b < b.b) && (l == b.l)) {
                if((h < b.h) && (b == b.b) && (l == b.l))
                    return true;
            }
        }
        return false;
    }
    ostream operator << (ostream o, Box b) {
        o << b.l << " " << b.b << " " << b.h;
        return o;
    }
};


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}

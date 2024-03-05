import 'dart:async';
import 'dart:io';

void main(){
File('lastUsed.txt').readAsString().then((String cons){ print(cons);});}

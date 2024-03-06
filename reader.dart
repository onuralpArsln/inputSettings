import 'dart:async';
import 'dart:io';

void main() {
  String name = "7824378634278423";
  File('lastUsed.txt').readAsString().then((String cons) {
    print(cons);
    name = cons;
  });
  print("name is here");
  print(name);
}

import 'dart:io';
import 'dart:convert';

// bu senkron

void main() async {
  var process = await Process.start('python3', ['doubleDetect.py']);
  await process.stdout.transform(utf8.decoder).forEach(print);

  print("haloo darknes");
}

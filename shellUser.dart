import 'dart:io';
import 'dart:convert';

void main() async {
  var process = await Process.start('python3', ['doubleDetect.py']);
  await process.stdout.transform(utf8.decoder).forEach(print);
}

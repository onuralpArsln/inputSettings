import 'dart:io';
import 'dart:convert';

void main() {
  Process.start('python3', ['doubleDetect.py']).then((Process process) {
    print('Python process started with pid ${process.pid}');
    process.stdout.transform(utf8.decoder).listen((data) {
      print('Python stdout: $data');
    });
    process.stderr.transform(utf8.decoder).listen((data) {
      print('Python stderr: $data');
    });
    // Optionally, you can listen for the process exit event
    process.exitCode.then((int code) {
      print('Python process exited with code $code');
    });
  }).catchError((error) {
    print('Failed to start Python process: $error');
  });
  // Continue with Dart code while Python process runs in the background
  print('Dart code continues executing...');
}

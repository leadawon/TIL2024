import 'package:flutter/material.dart';
//import 'package:hansori1/screen/login_screen.dart';

class EmailVerificationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Email Verification'),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'An email has been sent to your email address. '
                  'Please check your email and follow the instructions to verify your account.',
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 24.0),
            ElevatedButton(
              onPressed: () {
                // 사용자가 이메일을 확인한 후 로그인 화면으로 이동
                Navigator.popUntil(context, (route) => route.isFirst);
              },
              child: Text('Verified'),
            ),
            TextButton(
              onPressed: () {
                // TODO: 추가적인 이메일 인증 요청 로직 구현
              },
              child: Text('Resend Email'),
            ),
          ],
        ),
      ),
    );
  }
}

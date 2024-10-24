import 'package:firebase_signin/my_button/my_button.dart';
import 'package:flutter/material.dart';

class LogIn extends StatelessWidget {
  const LogIn({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: Text(
          'Sign In',
          style: TextStyle(color: Colors.white),
        ),
        centerTitle: true,
        elevation: 0.2,
      ),
      body: _buildButton(),
    );
  }

  Widget _buildButton() {
    return Padding(
      padding: EdgeInsets.all(16.0),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          MyButton(
            image: Image.asset('asset/img/glogo.png'),
            text: Text(
              'Login with Google',
              style: TextStyle(color: Colors.black87, fontSize: 15.0),
            ),
            color: Colors.white,
            radius: 4.0,
            onPressed: () {},
          ),
          SizedBox(
            height: 10.0,
          ),
          ButtonTheme(
            height: 50.0,
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                backgroundColor: Color(0xFF334D92),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(
                    Radius.circular(4.0),
                  ),
                ),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  Image.asset('asset/img/flogo.png'),
                  Text(
                    'Login with Facebook',
                    style: TextStyle(color: Colors.white, fontSize: 15.0),
                  ),
                  Opacity(
                    opacity: 0.0,
                    child: Image.asset('asset/img/glogo.png'),
                  ),
                ],
              ),
            ),
          ),

          SizedBox(
            height: 10.0,
          ),
          ButtonTheme(
            height: 50.0,
            child: ElevatedButton(
              onPressed: () {},
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.green,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(
                    Radius.circular(4.0),
                  ),
                ),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  Icon(
                    Icons.mail,
                    color: Colors.white,
                  ),
                  Text(
                    'Login with Email',
                    style: TextStyle(color: Colors.white, fontSize: 15.0),
                  ),
                  Opacity(
                    opacity: 0.0,
                    child: Icon(
                      Icons.mail,
                      color: Colors.white,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

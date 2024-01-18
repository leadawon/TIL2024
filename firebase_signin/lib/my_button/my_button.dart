import 'package:flutter/material.dart';

import '../login_app/login.dart';

class MyButton extends StatelessWidget {



  const MyButton({Key? key,required this.image,required this.text,required this.color,required this.radius,required this.onPressed}):super(key:key);

  final Widget image;
  final Widget text;
  final Color color;
  final double radius;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {



    return ButtonTheme(
      height: 50.0,
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: color,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(radius),
            ),
          ),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: <Widget>[
            image,
            text,
            Opacity(
              opacity: 0.0,
              child: Image.asset('asset/img/glogo.png'),
            ),
          ],
        ),
      ),
    );
  }
}

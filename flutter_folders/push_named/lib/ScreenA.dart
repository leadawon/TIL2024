import 'package:flutter/material.dart';

class ScreenA extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        title: Text('ScreenA'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              style:ElevatedButton.styleFrom(backgroundColor: Colors.blue),
              child:Text('Go to ScreenB'),
              onPressed: (){
                Navigator.pushNamed(context, '/b');
              }
            ),
            ElevatedButton(
                style:ElevatedButton.styleFrom(backgroundColor: Colors.blue),
                child:Text('Go to ScreenC'),
                onPressed: (){
                  Navigator.pushNamed(context, '/c');

                  // Navigator.pushNamed(
                  //   context,
                  //   '/c',
                  //   arguments: {'useremail': email},
                  // ); <-- 매개변수 넘기기
                }
            ),
          ],
        ),
      ),
    );
  }
}
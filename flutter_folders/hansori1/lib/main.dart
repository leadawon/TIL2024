import 'package:flutter/material.dart';
import 'package:hansori1/screen/login_screen.dart';
//import 'package:hansori1/screen/home_screen.dart';

void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  final bool isLoggedIn = false;

  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: 'Hansori1',
      home: LoginScreen(),
    );
  }
}
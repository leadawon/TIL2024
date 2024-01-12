// import 'package:flutter/material.dart';
// import 'package:hansori/screen/signup_screen.dart';
// import 'dart:convert';
// import 'package:http/http.dart' as http;
// import 'package:hansori/screen/home_screen.dart';
//
// class LoginScreen extends StatefulWidget {
//   const LoginScreen({Key? key}) : super(key: key);
//
//   @override
//   _LoginScreenState createState() => _LoginScreenState();
// }
//
// class _LoginScreenState extends State<LoginScreen> {
//   final TextEditingController _emailController = TextEditingController();
//   final TextEditingController _passwordController = TextEditingController();
//
//   Future<void> _login() async {
//     final String email = _emailController.text;
//     final String password = _passwordController.text;
//
//     // final response = await http.post(
//     //   Uri.parse('http://your-backend-url.com/login'), // 백엔드 URL 수정 필요
//     //   headers: <String, String>{
//     //     'Content-Type': 'application/json',
//     //   },
//     //   body: jsonEncode(<String, String>{
//     //     'password': password,
//     //     'email': email,
//     //   }),
//     // );
//
//     // 가상의 응답 생성
//     // 백엔드 구현이 완료되면 실제 HTTP 요청으로 대체
//     final response = http.Response(
//       jsonEncode({'result': true}), // true 또는 false로 변경하여 테스트
//       200, // HTTP 상태 코드
//       headers: {
//         'Content-Type': 'application/json',
//       },
//     );
//
//     // 응답 처리
//     if (response.statusCode == 200) {
//       final responseJson = jsonDecode(response.body);
//       if (responseJson['result']) {
//         // 로그인 성공, 홈 화면으로 이동
//         Navigator.pushReplacement(
//           context,
//           MaterialPageRoute(builder: (context) => HomeScreen(useremail: email)),
//         );
//       } else {
//         // 로그인 실패
//         _showDialog('Login failed. Please check your credentials.');
//       }
//     } else {
//       // 서버 에러 또는 기타 오류
//       _showDialog('Error: ${response.statusCode}');
//     }
//   }
//
//   void _showDialog(String message) {
//     showDialog(
//       context: context,
//       builder: (BuildContext context) {
//         return AlertDialog(
//           title: Text('Login Error'),
//           content: Text(message),
//           actions: <Widget>[
//             TextButton(
//               child: Text('Close'),
//               onPressed: () {
//                 Navigator.of(context).pop();
//               },
//             ),
//           ],
//         );
//       },
//     );
//   }
//
//   void _signup() {
//     Navigator.push(
//       context,
//       MaterialPageRoute(builder: (context) => SignupScreen()),
//     );
//   }
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       //backgroundColor: Colors.grey,
//       //resizeToAvoidBottomInset: false,
//       appBar: AppBar(
//         title: Text(
//           'Hansori Discord',
//           style: TextStyle(
//             //color: Colors.amber,
//             //letterSpacing: 2.0,
//             //fontSize: 28.0,
//             //fontWeight: FontWeight.bold,
//           ),
//         ),
//         //centerTitle: true,
//         //backgroundColor: Colors.redAccent,
//         //elevation:0.0,
//       ),
//       body: Padding(
//         padding: EdgeInsets.all(16.0),
//         // EdgeInsets.fromLTRB(Left, Top, Right, Bottom)
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: <Widget>[
//             //Icon(Icons.check_circle_outline),
//             //CircleAvatar(backgroundImage: AssetImage(assetName), radius: 60.0, backgroundColor: Colors.amber), <- 이거 Center위젯으로 감싸기
//             TextFormField(
//               // TODO: 이메일 형태체크하는 코드
//               controller: _emailController,
//               decoration: InputDecoration(
//                 labelText: 'Email',
//                 border: OutlineInputBorder(),
//               ),
//             ),
//             SizedBox(height: 16.0),
//             TextFormField(
//               controller: _passwordController,
//               obscureText: true,
//               decoration: InputDecoration(
//                 labelText: 'Password',
//                 border: OutlineInputBorder(),
//               ),
//             ),
//             SizedBox(height: 20.0),
//             Row(
//               mainAxisAlignment: MainAxisAlignment.center, // center, end, start
//               children: <Widget>[
//                 ElevatedButton(
//                   onPressed: _login,
//                   child: Text('Login'),
//                 ),
//                 SizedBox(width: 16.0),
//                 ElevatedButton(
//                   onPressed: _signup,
//                   child: Text('Signup'),
//                 ),
//               ],
//             ),
//           ],
//         ),
//       ),
//     );
//   }
//
//   @override
//   void dispose() {
//     _emailController.dispose();
//     _passwordController.dispose();
//     super.dispose();
//   }
// }
//
// class MyPage extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//         appBar: AppBar(
//           title: Text("text"),
//           centerTitle: true,
//           elevation: 0.0,
//           leading: IconButton(
//             // leading은 왼쪽에 배치할때 쓴다.
//             icon: Icon(Icons.menu), // <- 햄버거 메뉴
//             onPressed: () {
//               print('menu button is clicked');
//             },
//           ),
//           actions: [
//             IconButton(
//               icon: Icon(Icons.shopping_cart),
//               onPressed: () {
//                 print('Search button is clicked');
//               },
//             )
//           ],
//         ),
//         drawer: Drawer(
//           child: ListView(
//             padding: EdgeInsets.zero, // 여백없음
//             children: <Widget>[
//               UserAccountsDrawerHeader(
//                   currentAccountPicture: CircleAvatar(
//                     backgroundImage: AssetImage('asset/img/img.png'),
//                     backgroundColor: Colors.white,
//                   ),
//                   otherAccountsPictures: <Widget>[
//                     CircleAvatar(
//                       backgroundImage: AssetImage('asset/img/img.png'),
//                       backgroundColor: Colors.white,
//                     ),
//                     // CircleAvatar(
//                     //   backgroundImage: AssetImage('asset/img/img.png'),
//                     //   backgroundColor: Colors.white,
//                     // ),
//                   ],
//                   accountName: Text('asd'),
//                   accountEmail: Text('asd'),
//                   onDetailsPressed: () {
//                     print('arrow is clicked');
//                   },
//                   decoration: BoxDecoration(
//                       color: Colors.red[200],
//                       borderRadius: BorderRadius.only(
//                         bottomLeft: Radius.circular(40.0),
//                         bottomRight: Radius.circular(40.0),
//                       ))),
//               ListTile(
//                 leading: Icon(
//                   Icons.home,
//                   color: Colors.grey[850],
//                 ),
//                 title: Text('Hone'),
//                 onTap: () {
//                   print('Home is clicked');
//                 },
//                 trailing: Icon(Icons.add), // 오른쪽에 붙이기.
//               ),
//               ListTile(
//                 leading: Icon(
//                   Icons.question_answer, // setting...
//                   color: Colors.grey[850],
//                 ),
//                 title: Text('q&a'),
//                 onTap: () {
//                   print('q&a is clicked');
//                 },
//                 trailing: Icon(Icons.add), // 오른쪽에 붙이기.
//               ),
//             ],
//           ),
//         ),
//         body: Builder(
//           builder: (BuildContext ctx){
//             return Center(
//               child: FlatButton(
//                 child: Text(
//                   'Show me',
//                   style: TextStyle(color: Colors.black),
//                 ),
//                 color: Colors.red,
//                 onPressed: () {
//                   Scaffold.of(ctx).showSnackBar(SnackBar( // context 그냥 쓰면 부모인 MyPage의 context임. 얘는 scaffold가 없음
//                     content: Text('hello'),
//                   ));
//                 },
//               ),
//             );
//           },
//         ));
//   }
// }
//
// class MyPage2 extends StatelessWidget{
//   @override
//   Widget build(BuildContext context){
//     return Center(
//         child: RaisedButton(
//             child: Text('show me'),
//             onPressed: (){
//               Scaffold.of(context).showSnackBar(SnackBar(
//                 context: Text('Hello',
//                   textAlign: TextAlign.center,
//                   style: TextStyle(
//                     color: Colors.white,
//                   ),
//                 ),
//                 backgroundColor:  Colors.teal,
//                 duration: Duration(milliseconds: 1000),
//               ),
//               );
//             }
//         )
//     );
//   }
// }
//
//
// //cupertino_icons 밑에 fluttertoast 추가
// class MyPage3 extends StatelessWidget{
//   @override
//   Widget build(BuildContext context){
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Toast message'),
//         centerTitle: true,
//       ),
//       body: Center(
//         child: FlatButton(
//           onPressed: (){},
//           child: Text('Toast'),
//         ),
//       ),
//     );
//   }
// }
// // import 해야함!!!!
// void flutterToast(){
//   Fluttertoast.showToast(msg: 'Flutter',
//       gravity: ToastGravity.BOTTOM,
//       backgroundColor: Colors.redAccent,
//       fontSize: 20.0,
//       textColor: Colors.white,
//       toastLength: Toast.LENGTH_SHORT);
// }
//
// //--------
//
// class MyPage3 extends StatelessWidget{
//   @override
//   Widget build(BuildContext context){
//     return Scaffold(
//       backgroundColor: Colors.blue,
//       body: SafeArea(
//         child: Container( // Container는 자식에 없으면 최대한으로 영향을 준다. 자식이 있으면 자식으로 줄어든다.
//           color: Colors.red, // 이거까지 하면 scaffold에서 blue로 지정하더라도 red를 먹음
//           child: Text('Hello'), // 이거하면 텍스트 바깥은 blue 텍스트의 배경색은 red가 된다.
//           width: 100,
//           height: 100,
//           margin: EdgeInsets.all(20), // EdgeInsets.symmetric(vertical, horizontal) <- 위쪽
//         ),
//       ),
//     );
//   }
// }
//
//
// //-----
//
//
// class MyPage4 extends StatelessWidget{
//   @override
//   Widget build(BuildContext context){
//     return Scaffold(
//       backgroundColor: Colors.teal,
//       body: SafeArea(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.spaceBetween,
//           crossAxisAlignment: CrossAxisAlignment.center,
//           //mainAxisSize: MainAxisSize.min, // 이러면 Center가 통제권 다시 가져서 상하좌우 센터함.
//
//           children: <Widget>[
//             Container(
//                 child: Text('Container 1');
//             ),
//             Container(
//                 child: Text('Container 2');
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
//
//
// //---------------
//
// class FirstPage extends StatelessWidget{
//   @override
//   Widget build(BuildContext context2){
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('First page'),
//       ),
//       body: Center(
//         child: RaiseButton(
//             child: Text('Go to the Second page'),
//
//             onPressed: (){
//               Navigator.push(context2, MaterialPageRoute(
//                   builder:(BuildContext context){return SecondPage();} // 빌더(BuildContext context) 사용할필요 없으면 안써도 된다.
//               ));
//             }
//         ),
//       ),
//     );
//   }
// }
//
// class SecondPage extends StatelessWidget{
//   @override
//   Widget build(BuildContext ctx){
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Second page'),
//       ),
//       body: Center(
//         child: RaiseButton(
//             child: Text('Go to the First page'),
//
//             onPressed: (){
//               Navigator.pop(ctx);
//             }
//         ),
//       ),
//     );
//   }
// }
//
// //----------------
//
//
//
//
// // ctrl alt L <- formatting

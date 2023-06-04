import 'package:daily_diet_date/milestone.dart';
import 'package:daily_diet_date/sign_in.dart';
import 'package:flutter/material.dart';
import 'sign_up.dart';
import 'reward.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
          body: SafeArea(
        child: SignUp()
        // child: MilestonePage(),
        // child: Reward(),
      )),
    );
  }
}

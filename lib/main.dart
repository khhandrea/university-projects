import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math';
import 'package:intl/intl.dart';
import 'package:daily_diet_date/milestone.dart';
import 'package:daily_diet_date/sign_in.dart';
import 'package:flutter/material.dart';
import 'sign_up.dart';
import 'reward.dart';
import 'view_profile.dart';
import 'profile.dart';

class Challenge {
  final String category;
  final String description;

  Challenge({required this.category, required this.description});
}
final List<String> userInputList = [];
List<Challenge> weightLossChallenges = [
  Challenge(category: 'Weight Loss', description: 'Take a 30-minute brisk walk today.'),
  Challenge(category: 'Weight Loss', description: 'Replace sugary drinks with water for the entire day.'),
  Challenge(category: 'Weight Loss', description: 'Do 10 minutes of high-intensity interval training (HIIT).'),
  // Add more weight loss challenges
];

List<Challenge> healthyEatingChallenges = [
  Challenge(category: 'Healthy Eating', description: 'Eat at least five servings of fruits and vegetables today.'),
  Challenge(category: 'Healthy Eating', description: 'Cook a healthy homemade meal for dinner.'),
  Challenge(category: 'Healthy Eating', description: 'Choose whole grain options for your breakfast.'),
  // Add more healthy eating challenges
];

List<Challenge> healthyLifestyleChallenges = [
  Challenge(category: 'Healthy Lifestyle', description: 'Practice meditation or deep breathing for 10 minutes.'),
  Challenge(category: 'Healthy Lifestyle', description: 'Get at least 8 hours of quality sleep tonight.'),
  Challenge(category: 'Healthy Lifestyle', description: 'Take a break from screens and engage in a hobby or physical activity.'),
  // Add more healthy lifestyle challenges
];

Challenge getChallengeBasedOnTime(List<Challenge> challenges) {
  final DateTime now = DateTime.now();
  final int day = now.day;
  final Challenge selectedChallenge = challenges[day % challenges.length];
  return selectedChallenge;
}
void main() {
  final weightLossChallenge = getChallengeBasedOnTime(weightLossChallenges);
  final healthyEatingChallenge = getChallengeBasedOnTime(healthyEatingChallenges);
  final healthyLifestyleChallenge = getChallengeBasedOnTime(healthyLifestyleChallenges);
  // Generate challenges based on the current time of the day
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Navigation',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: {
        '/': (context) => MainPage(), // Set the main page as the home
        SignIn.routeName: (context) => SignIn(),
        Edit_profile.routeName: (context) => Edit_profile(),
        SignUp.routeName: (context) => SignUp(),
        View_ProfilePage.routeName: (context) => View_ProfilePage(userInputList: [],)
      },
    );
  }
}

class MainPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Widget getInfoSection = Card();
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Colors.green.shade400, Colors.white],
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Image.asset(
              'assets/welcome.png',
              height: 150,
            ),
            SizedBox(height: 16),
            Image.asset(
              'assets/robot.png',
              height: 200,
            ),
            SizedBox(height: 16),
            Column(
              children: [
                SizedBox(height: 16),
                Column(
                  children: [
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => SignIn(),
                          ),
                        );
                      },
                      child: SizedBox(
                        width: 300,
                        height: 50,
                        child: Image.asset(
                          'assets/login.png',
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                    SizedBox(height: 16),
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => SignUp(),
                          ),
                        );
                      },
                      child: SizedBox(
                        width: 300,
                        height: 50,
                        child: Image.asset(
                          'assets/signup.png',
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}



import 'package:flutter/material.dart';
import 'home.dart';

class Reward extends StatelessWidget {
  const Reward({super.key});
  static const routeName = '/reward';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('My Rewards'),
        leading: IconButton(
          icon: Image.asset(
    'assets/avatar-8Aa.png',
    width: 150,
    height: 150,
  ),
          onPressed: () {
            // Navigate to profile page
            print('navigate to profile page');
          },
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.arrow_back),
            onPressed: () {
              // Navigate to profile page
              Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const Scene()),
        );
            },
          ),
        ],
        toolbarHeight: 100,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(
            bottom: Radius.circular(20),
          ),
        ),
        backgroundColor: const Color.fromRGBO(145, 209, 104, 1),
      ),
      body: Container(
        color: const Color.fromRGBO(248, 250, 255, 1),
        padding: const EdgeInsets.all(18.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(
              flex: 1,
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.all(8.0),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(4.0),
                  color: const Color.fromRGBO(255, 255, 255, 1),
                ),
                child: const Row(
                  children: [
                    Icon(Icons.check),
                    SizedBox(width: 8),
                    Text(
                      '★ 300 points till next reward',
                      style: TextStyle(fontSize: 16),
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 16),
            const Text(
              'Available rewards',
              style: TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 16),
            Expanded(
              flex: 4,
              child: Container(
                color: const Color.fromRGBO(255, 255, 255, 1),
                child: ListView(
                  children: [
                    RewardBox(
                      key: UniqueKey(),
                      image: 'assets/starbucks-logo.png',
                      text: 'Starbucks Coupon',
                      point: 500,
                      onPressed: () {
                        // Handle reward button pressed
                        print('Got Starbucks coupon!');
                      },
                    ),
                    RewardBox(
                      key: UniqueKey(),
                      image: 'assets/starbucks-logo.png',
                      text: 'Olive Young Voucher',
                      point: 1000,
                      onPressed: () {
                        // Handle reward button pressed
                        print('Got Olive Young voucher!');
                      },
                    ),
                    // Add more RewardBox widgets for each reward
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class RewardBox extends StatelessWidget {
  final String image;
  final String text;
  final int point;
  final VoidCallback onPressed;

  const RewardBox({
    required Key key,
    required this.image,
    required this.text,
    required this.point,
    required this.onPressed,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 80,
      child: Card(
        color: const Color.fromRGBO(233, 255, 235, 1),
        child: ListTile(
          leading: Image.asset(
            image,
            width: 64,
            height: 64,
          ),
          title: Text(
            text,
            style: const TextStyle(
              color: Color.fromRGBO(136, 202, 94, 1),
              fontSize: 18,
            ),
          ),
          subtitle: Text(
            "$point Points",
            style: const TextStyle(
              color: Color.fromRGBO(0, 0, 0, 1),
              fontSize: 12,
            ),
          ),
          trailing: const Icon(Icons.check),
          onTap: onPressed,
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';
import 'package:mobile/features/onboarding/presentation/pages/phone.verification.dart';
import 'package:mobile/features/piggies/presentation/pages/dashboard.dart';
import 'package:mobile/features/shared/presentation/pages/welcome.dart';
import 'package:modal_bottom_sheet/modal_bottom_sheet.dart';
import 'package:shared_utils/shared_utils.dart';

class AppRouterConfig {
  static Route<dynamic>? setupRoutes(RouteSettings settings) {
    switch (settings.name) {
      case AppRouter.welcomeRoute:
        return MaterialWithModalsPageRoute(
            builder: (_) => const WelcomePage(), settings: settings);
      case AppRouter.dashboardRoute:
        return MaterialWithModalsPageRoute(
            builder: (_) => const DashboardPage(), settings: settings);
      case AppRouter.phoneVerificationRoute:
        return MaterialWithModalsPageRoute(
            builder: (_) => const PhoneNumberVerificationPage(),
            settings: settings);
    }

    return MaterialPageRoute(
      builder: (context) => Scaffold(
        appBar: AppBar(
            elevation: 0, backgroundColor: context.colorScheme.background),
        body: const EmptyContentPlaceholder(
          icon: TablerIcons.mood_empty,
          title: 'Oops...you seem far from home',
          subtitle:
              'An error occurred while getting your content. Please try again later',
        ),
      ),
    );
  }
}

class AppRouter {
  static const welcomeRoute = '/';
  static const dashboardRoute = '/dashboard';
  static const phoneVerificationRoute = '/phone-verification';
  static const savingsRoute = '/savings'; // todo
  static const savingsDetailsRoute = '/savings-info'; // todo
  static const piggiesRoute = '/my-piggies'; // todo
  static const notificationsRoute = '/notifications-&-reminders'; // todo
  static const supportServiceRoute = '/help-center'; // todo
  static const budgetingToolsRoute = '/budgeting-tools'; // todo
}

import 'package:auto_route/auto_route.dart';
import 'package:flutter/material.dart';
import 'package:mobile/core/di/injection.dart';
import 'package:mobile/core/utils/constants.dart';
import 'package:mobile/protos/bank.pbgrpc.dart';
import 'package:mobile/protos/savings.pbgrpc.dart';
import 'package:protobuf_google/protobuf_google.dart';
import 'package:shared_utils/shared_utils.dart';

import '../../../../protos/customer.pbgrpc.dart';

/// welcome page for all users
@RoutePage()
class WelcomePage extends StatefulWidget {
  const WelcomePage({Key? key}) : super(key: key);

  @override
  State<WelcomePage> createState() => _WelcomePageState();
}

class _WelcomePageState extends State<WelcomePage> {
  @override
  void initState() {
    super.initState();
    _testGrpc();
  }

  @override
  Widget build(BuildContext context) {
    kUseDefaultOverlays(context, statusBarBrightness: context.theme.brightness);
    return Scaffold(
      body: Column(
        children: [
          Expanded(child: Container()),
          AnimatedColumn(
            animateType: AnimateType.slideUp,
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              kAppName.h6(context),
              kAppDesc.subtitle2(context).top(8).bottom(40),
              SafeArea(
                top: false,
                child: AppRoundedButton(
                  text: 'Start saving now',
                  icon: TablerIcons.coin_pound,
                  // TODO: home page
                  onTap: () {},
                ).align(Alignment.centerRight),
              ),
            ],
          ).horizontal(24),
        ],
      ),
    );
  }

  void _testGrpc() async {
    var savingsClient = getIt<SavingsServiceClient>();
    savingsClient
        .listSavings(ListSavingsRequest(customerId: 'hello', piggybankId: 'gi'))
        .listen((value) {
      logger.d('savings accounts: $value');
    });

    var bankClient = getIt<PiggyBankServiceClient>();
    bankClient.listPiggyBanks(Empty()).listen((value) {
      logger.d('piggies: $value');
    });

    var customerClient = getIt<CustomerServiceClient>();
    customerClient.getCurrentCustomer(Empty()).listen((value) {
      logger.d('current customer: $value');
    });
  }
}

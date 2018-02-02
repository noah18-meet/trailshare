function WelcomeAlert() {
            var currentDate = new Date();
            var currentHour = currentDate.getHours();
            var str;
            if (currentHour > 6 && currentHour <= 12) {
                str = "Good Morning";
            }
            else if (currentHour > 12 && currentHour <= 17) {
                str = "Good Afternoon!";
            }
            else if (currentHour > 17 && currentHour <= 22) {
                str = "Good Evening";
            }
            else {
                str = "Good Night";

            }
            alert(str);
        }
        WelcomeAlert();
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # DP[i] = number of new people who learned the secret on day i
        DP = [0] * (n + 1)
        DP[1] = 1  # 1 person knows it on day 1
        peopleSharingSecrets = 0
        MOD = 10 ** 9 + 7

        # Go through to day n and calculate new people learning secret each day
        for curTime in range(2, n + 1):
            # Add people who start sharing
            if curTime - delay >= 1:
                peopleSharingSecrets = (peopleSharingSecrets + DP[curTime - delay]) % MOD

            # Subtract people who forget
            if curTime - forget >= 1:
                peopleSharingSecrets = (peopleSharingSecrets - DP[curTime - forget] + MOD) % MOD

            # Record new people learning secret on current day
            DP[curTime] = peopleSharingSecrets

        # Count total people who know the secret on day n
        # This includes everyone who learned in range [max(1, n-forget+1), n]
        peopleAware = 0
        for i in range(max(1, n - forget + 1), n + 1):
            peopleAware = (peopleAware + DP[i]) % MOD

        return peopleAware
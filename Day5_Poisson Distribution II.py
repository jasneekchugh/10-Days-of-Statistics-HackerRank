
lambdas = list(map(float, input().split()))
lambda1 = lambdas[0]
lambda2 = lambdas[1]

# Gets the result and show on the screen
print (round(160 + 40 * (lambda1 + lambda1 ** 2), 3))
print (round(128 + 40 * (lambda2 + lambda2 ** 2), 3))
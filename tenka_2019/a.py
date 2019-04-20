A, B, C = map(int, input().split())

if A<C and C < B:
    print('Yes')
elif C<A and B<C:
    print('Yes')
else:
    print('No')
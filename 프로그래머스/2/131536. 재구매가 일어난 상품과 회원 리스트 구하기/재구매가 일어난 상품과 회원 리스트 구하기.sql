-- 코드를 입력하세요
SELECT USER_ID,PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID ASC,PRODUCT_ID DESC;
#동일한 회원이 동일한 상품을 재구매한 데이터 
#재구매한 회원 ID와 재구매한 상품 ID 출력하는 SQL
#회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.
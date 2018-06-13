### 饿了么
---

```
---每家店的月收入
SELECT
	a.restaurant_id,
	  round(sum(a.month_sales * a.price) / 10000, 2) AS total_money,
	b.NAME 
FROM
	restaurant_foods a
	LEFT JOIN elm_new b ON a.restaurant_id = b.ele_id 
GROUP BY
	a.restaurant_id,
	b.NAME 
ORDER BY
	total_money DESC
```
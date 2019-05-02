$fn = fn($x = 0) => $x + 1;

~~~

$fn = function ($x = 0) {
    return $x + 1;
};

---

array_map(fn(int $n, float $m) => $n + $m, $array1, $array2);

~~~

array_map(
    function (int $n, float $m) {
        return $n + $m;
    },
    $array1,
    $array2
);

---

$fn = fn($x) => $x + 1;

~~~

$fn = function ($x) {
    return $x + 1;
};

---

array_map(fn($a) => {
    return strtoupper($a);
}, $array1);

~~~

array_map(function ($a) {
    return strtoupper($a);
}, $array1);

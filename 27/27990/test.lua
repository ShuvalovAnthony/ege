local f = io.open("/Users/anton/Documents/ez_python/ege/27/27990/27990_B.txt", "r")


if f then
    local n = tonumber(f:read())

    local nums = {}

    for line in f:lines() do
        table.insert(nums, tonumber(line))
    end

    f:close()

    local counter = 0

    for i = 1, #nums - 1 do
        for j = i + 1, #nums do
            if nums[i] and nums[j] and nums[i] * nums[j] % 62 == 0 then
                counter = counter + 1
            end
        end
    end

    print(counter)
else
    print("Ошибка: не удалось открыть файл.")
end

require 'date'

class User
    attr_reader :name, :date_of_birth

    def initialize(name, date_of_birth)
        @name = name
        @date_of_birth = date_of_birth
    end

    def age
        # find difference between today and birth-date
        difference = Date.today - date_of_birth
        # immediately returns an integer representing days, simply divide and floor
        return (difference / 365).floor
    end
    
    def next_birthday
        # create this year's birthday
        bday = Date.new(Date.today.year, date_of_birth.month, date_of_birth.day)
        # if bday has not happened, it is the next birthday
        if bday >= Date.today
            return bday
        # if it has, next year's is the next
        else 
            return bday.next_year
        end
    end

end

tests = [
    Date.new(1986, 1, 1),
    Date.new(1988, Date.today.month, Date.today.day),
    Date.new(1998, 12, 30),
]

puts
tests.each do |date|
    puts "#{date} => #{User.new("Test", date).age}"
end

puts
tests.each do |date|
    puts "#{date} => #{User.new("Test", date).next_birthday}"
end